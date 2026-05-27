from django.shortcuts import render, redirect, get_object_or_404

from .models import *

import qrcode

from io import BytesIO

from django.core.files import File

from django.contrib import messages



# =========================
# BOOKING PAGE
# =========================

def booking_page(request, id):

    event = get_object_or_404(Event, id=id)



    if request.method == "POST":

        full_name = request.POST.get('full_name')

        email = request.POST.get('email')

        phone = request.POST.get('phone')

        seats = request.POST.get('seats')



        # SEAT LIMIT CHECK

        booked_seats = Booking.objects.filter(
            event=event
        ).count()



        if booked_seats >= event.total_seats:

            messages.error(
                request,
                "No seats available"
            )

            return redirect(
                'booking_page',
                id=event.id
            )



        # CREATE BOOKING

        booking = Booking.objects.create(
            event=event,
            full_name=full_name,
            email=email,
            phone=phone,
            seats=seats
        )



        # QR DATA

        qr_data = f"""
        Booking ID: {booking.booking_id}
        Name: {booking.full_name}
        Event: {booking.event.title}
        Seats: {booking.seats}
        """



        # GENERATE QR

        qr_image = qrcode.make(qr_data)

        qr_offset = BytesIO()

        qr_image.save(
            qr_offset,
            format='PNG'
        )



        file_name = f'{booking.booking_id}.png'



        # SAVE QR CODE

        booking.qr_code.save(
            file_name,
            File(qr_offset),
            save=True
        )



        # REDIRECT TO TICKET PAGE

        return redirect(
            'ticket_page',
            booking.id
        )



    context = {
        'event': event
    }

    return render(
        request,
        'booking.html',
        context
    )




# =========================
# SUCCESS PAGE
# =========================

def booking_success(request):

    return render(
        request,
        'success.html'
    )
from django.contrib import admin
from .models import Event, Booking


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'date',
        'location',
        'total_seats'
    )

    search_fields = (
        'title',
        'category',
        'location'
    )

    list_filter = (
        'category',
        'date'
    )




@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'event',
        'seats',
        'booking_date'
    )

    search_fields = (
        'full_name',
        'email'
    )

    list_filter = (
        'booking_date',
    )