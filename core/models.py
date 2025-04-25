# models.py - Defines database structure for Show and Booking in Django

from django.db import models

# Model representing a Show (event or movie)
class Show(models.Model):
    name = models.CharField(max_length=100)                         # Title of the show
    date = models.DateField()                                       # Scheduled date of the show
    time = models.TimeField()                                       # Scheduled time of the show
    venue = models.CharField(max_length=100)                        # Location/venue of the show
    total_seats = models.IntegerField()                             # Total number of seats available
    available_seats = models.IntegerField()                         # Seats currently available for booking
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Price per ticket

    def __str__(self):
        return self.name                                            # String representation (name of show)


# Model representing a Booking made by a user for a show
class Booking(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Link to the user who booked
    show = models.ForeignKey(Show, on_delete=models.CASCADE)         # Link to the booked show
    seats = models.IntegerField()                                    # Number of seats booked
    booking_date = models.DateTimeField(auto_now_add=True)           # Date and time when booking was created
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total price of booking

    def __str__(self):
        return f"{self.user.username} - {self.show.name} - {self.seats} seats"  # String output for admin/debug
