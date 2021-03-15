from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Category, AuctionListings, Bids, Comments

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(AuctionListings)
admin.site.register(Bids)
admin.site.register(Comments)