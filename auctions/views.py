from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib import messages

from .models import User, Category, AuctionListings, Bids, Comments

class createAuction(forms.Form):
    category = forms.MultipleChoiceField(widget=
        forms.SelectMultiple(attrs={ 'class': 'form-control'}),
        choices=tuple((x.id, x) for x in Category.objects.all())        
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    bid = forms.IntegerField(widget=
        forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bid amount'})
    )
    imageurl = forms.URLField(widget=
        forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Image on remote site' }),
        required=False
    )

def index(request):
    l = AuctionListings.objects.filter(active=True)
    return render(request, "auctions/index.html", {
        "listings": l,
        "title": "Active Listings",
        "subtitle": "Active Listings",
        "empty": "There is no Active Listing currently."
    })

def allListings(request):
    l = AuctionListings.objects.all()
    return render(request, "auctions/index.html", {
        "listings": l,
        "title": "All Listings",
        "subtitle": "All Listings",
        "empty": "There is no any Listing currently."
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def createListing(request):
    if request.method == "POST":
        form = createAuction(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            imageurl = form.cleaned_data['imageurl']
            cat = Category.objects.filter(pk__in = form.cleaned_data["category"])
            A = AuctionListings(user=request.user, title=title, description=description, imageurl=imageurl)
            A.save()            
            B = Bids(user=request.user, amount=form.cleaned_data['bid'], listing=A)
            B.save()
            A.categories.add(*cat)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", { "form": createAuction(request.POST) })
    else:
        return render(request, "auctions/create.html", { "form": createAuction() })

def listing(request, id):
    l = AuctionListings.objects.get(pk=id)
    current = l.bids.last()
    if request.method == "POST":
        if 'watch_form' in request.POST:
            if request.user in l.watchers.all():
                l.watchers.remove(request.user)
            else:
                l.watchers.add(request.user)
        elif 'bid_form' in request.POST:
            if int(request.POST['amount']) <= current.amount:
                messages.error(request,'Your bid must be equal to or greater than the Current Bid!')
                return render(request, "auctions/listing.html", {
                    "item": l,
                    "current_bid": current
                })
            b = Bids(user=request.user, amount=int(request.POST['amount']), listing=l)                        
            b.save()
        elif 'comment_form' in request.POST:
            c = Comments(user=request.user, comment=request.POST['text'], listing=l)
            c.save()
        elif 'close_form' in request.POST:
            if current.user != request.user:
                l.winner = current.user
            l.active = False
            l.save()
        return HttpResponseRedirect(reverse("listing", args = (id,)))

    return render(request, "auctions/listing.html", {
        "item": l,
        "current_bid": current # Just to save multiple queries on the template side
    })

@login_required
def myListing(request):
    return render(request, "auctions/index.html", {
        "listings": request.user.listings.all(),
        "title": "My Listing",
        "subtitle": "My Auction Lists",
        "empty": "You haven't host any yet."
    })

@login_required
def won(request):
    return render(request, "auctions/index.html", {
        "listings": request.user.won.all(),
        "title": "Winings",
        "subtitle": "Your Winings",
        "empty": "You haven't won any yet."
    })

@login_required
def watchList(request):
    return render(request, "auctions/index.html", {
        "listings": request.user.watched.all(),
        "title": "Watchlist",
        "subtitle": "Watchlists",
        "empty": "You have no watched Auction yet."
    })

def cat_list(request, id):
    c = Category.objects.get(pk=id)
    return render(request, "auctions/index.html", {
        "listings": c.listings.all(),
        "title": c,
        "subtitle": f"All Listings under {c} Category",
        "empty": "No Auctions under this Category yet."
    })

def categories(request):
    return render(request, "auctions/categories.html", { "categories": Category.objects.all() })