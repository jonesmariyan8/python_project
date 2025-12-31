from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available')
    search_fields = ('title', 'location')
    list_filter = ('available', 'price')