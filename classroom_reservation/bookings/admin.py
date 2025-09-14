from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'capacity', 'available_hours', 'is_open')
    search_fields = ('code', 'name')
    list_filter = ('is_open',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'created_at')
    search_fields = ('user__username', 'room__code')
    readonly_fields = ('created_at',)
