# urls.py - URL configuration for the Django ticket booking system

from django.urls import path
from .views import (
    RegisterView,     # Handles user registration
    LoginView,        # Handles user login
    LogoutView,       # Handles user logout
    ShowListView,     # Displays list of all available shows
    BookTicketView,   # Allows users to book tickets for a selected show
    BookingHistoryView,  # Shows booking history of logged-in user
    AdminDashboardView,  # Dashboard for admin users only
    ManageShowsView,     # Admin view to add/edit/delete shows
    ViewBookingsView     # Admin view to see all bookings
)

# URL patterns mapping each view to a URL path
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),              # Registration page
    path('login/', LoginView.as_view(), name='login'),                       # Login page
    path('logout/', LogoutView.as_view(), name='logout'),                    # Logout user
    path('', ShowListView.as_view(), name='show_list'),                      # Home page showing list of shows
    path('book/<int:show_id>/', BookTicketView.as_view(), name='book_ticket'),  # Book ticket for a show
    path('history/', BookingHistoryView.as_view(), name='booking_history'),  # View booking history
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),    # Admin dashboard
    path('admin/shows/', ManageShowsView.as_view(), name='manage_shows'),    # Admin show management
    path('admin/bookings/', ViewBookingsView.as_view(), name='view_bookings') # Admin view of all bookings
]
