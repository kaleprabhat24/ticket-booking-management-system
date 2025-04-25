# ticket_booking/urls.py - URL routing for the project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # The '' pattern includes URLs from the 'core' app
    path('', include('core.urls')),  # Routes to core app's URL configurations
    
    # The admin path is used for accessing Django's admin interface (usually for superuser or admin tasks)
    path('admin/', admin.site.urls),  # Admin panel URL
]
