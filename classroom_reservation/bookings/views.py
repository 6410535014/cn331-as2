from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking
from .forms import BookRoomForm
from django.db import IntegrityError, transaction

def rooms_list(request):
    rooms = Room.objects.filter(is_open=True)
    return render(request, 'bookings/rooms_list.html', {'rooms': rooms, 'form': BookRoomForm()})


@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookRoomForm(request.POST)
        if form.is_valid():
            room = get_object_or_404(Room, pk=form.cleaned_data['room_id'])
            if not room.is_open:
                messages.error(request, 'ห้องนี้ปิดการจองแล้ว')
                return redirect('rooms')
            if room.available_hours <= 0:
                messages.error(request, 'ห้องนี้ไม่มีชั่วโมงว่างเหลือ')
                return redirect('rooms')
            try:
                with transaction.atomic():
                    booking = Booking.objects.create(user=request.user, room=room)
                    room.available_hours -= 1
                    room.save()
                messages.success(request, f'จองห้อง {room.code} สำเร็จ')
            except IntegrityError:
                messages.error(request, 'คุณได้จองห้องนี้ไปแล้ว (ได้สิทธิ์ 1 ชั่วโมงต่อห้อง)')
            return redirect('rooms')
    return redirect('rooms')


@login_required
def my_bookings(request):
    bookings = request.user.bookings.select_related('room')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    room = booking.room
    with transaction.atomic():
        booking.delete()
        room.available_hours += 1
        room.save()
    messages.success(request, f'ยกเลิกการจองห้อง {room.code} เรียบร้อย')
    return redirect('my_bookings')
