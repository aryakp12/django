# main/models.py

from django.db import models

class Booking(models.Model):
    arrival = models.DateField()
    departure = models.DateField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Booking from {self.arrival} to {self.departure} for {self.guests} guests'
