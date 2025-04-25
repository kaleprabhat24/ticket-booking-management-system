# admin.py - Registers models with Django admin panel for management

from django.contrib import admin
from .models import Show, Booking

# Register the Show model to make it manageable via Django Admin
admin.site.register(Show)

# Register the Booking model to allow booking records to be managed via admin panel
admin.site.register(Booking)
