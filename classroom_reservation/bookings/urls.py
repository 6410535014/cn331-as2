from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_list, name='rooms'),
    path('book/', views.book_room, name='book_room'),
    path('my/', views.my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
