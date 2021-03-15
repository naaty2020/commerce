from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newAuction", views.createListing, name="create"),
    path("listings/<int:id>", views.listing, name="listing"),
    path("mylistings", views.myListing, name="myListing"),
    path("won", views.won, name="won"),
    path("all-auctions", views.allListings, name="allListings"),
    path("Watched-Auctions", views.watchList, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:id>", views.cat_list, name="cat_list")
]
