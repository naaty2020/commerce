from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

class User(AbstractUser):
    pass

class FromModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True        

class Category(models.Model):    
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class AuctionListings(FromModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length = 32)
    description = models.TextField()
    imageurl = models.URLField(blank = True)
    categories = models.ManyToManyField(Category, blank=True, related_name="listings")
    watchers = models.ManyToManyField(User, blank=True, related_name="watched")
    winner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name="won")
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Bids(FromModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="bids")
    amount = models.PositiveIntegerField()

    class Meta:
        ordering = ['amount']
    
    def __str__(self):
        return f"{self.amount}"

class Comments(FromModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment