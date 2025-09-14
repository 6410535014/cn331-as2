from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    code = models.CharField(max_length=10, unique=True)   
    name = models.CharField(max_length=100)              
    capacity = models.PositiveIntegerField(default=1)     
    available_hours = models.PositiveIntegerField(default=0)  
    is_open = models.BooleanField(default=True)           

    def __str__(self):
        return f"{self.code} - {self.name}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'room'], name='one_booking_per_user_per_room')
        ]

    def __str__(self):
        return f"{self.user.username} -> {self.room.code} ({self.created_at:%Y-%m-%d %H:%M})"
