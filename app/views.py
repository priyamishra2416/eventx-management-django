from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.http import HttpResponse
from django.core.files import File

from reportlab.pdfgen import canvas

from io import BytesIO

import qrcode


# =========================
# HOME PAGE
# =========================

def home(request):

    events = Event.objects.all().order_by('-created_at')

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        events = events.filter(
            title__icontains=search
        )

    if category:
        events = events.filter(
            category__icontains=category
        )

    context = {
        'events': events
    }

    return render(request, 'home.html', context)


# =========================
# EVENT DETAIL PAGE
# =========================

def event_detail(request, id):

    event = get_object_or_404(Event, id=id)

    context = {
        'event': event
    }

    return render(request, 'event_detail.html', context)


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

        seats = int(seats)


        # TOTAL BOOKED SEATS

        booked_seats = Booking.objects.filter(
            event=event
        ).count()


        # SEAT LIMIT CHECK

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

        qr_image.save(qr_offset, format='PNG')

        file_name = f'{booking.booking_id}.png'


        # SAVE QR

        booking.qr_code.save(
            file_name,
            File(qr_offset),
            save=True
        )


        # REDIRECT TO TICKET

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
# QR TICKET PAGE
# =========================

def ticket_page(request, id):

    booking = get_object_or_404(
        Booking,
        id=id
    )

    context = {
        'booking': booking
    }

    return render(
        request,
        'ticket.html',
        context
    )


# =========================
# PDF DOWNLOAD
# =========================

def download_ticket(request, id):

    booking = get_object_or_404(
        Booking,
        id=id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="ticket_{booking.id}.pdf"'
    )

    p = canvas.Canvas(response)


    # TITLE

    p.setFont("Helvetica-Bold", 24)

    p.drawString(
        180,
        800,
        "Event Ticket"
    )


    # DETAILS

    p.setFont("Helvetica", 16)

    p.drawString(
        80,
        740,
        f"Event: {booking.event.title}"
    )

    p.drawString(
        80,
        700,
        f"Name: {booking.full_name}"
    )

    p.drawString(
        80,
        660,
        f"Email: {booking.email}"
    )

    p.drawString(
        80,
        620,
        f"Phone: {booking.phone}"
    )

    p.drawString(
        80,
        580,
        f"Seats: {booking.seats}"
    )

    p.drawString(
        80,
        540,
        f"Booking ID: {booking.booking_id}"
    )


    # FOOTER

    p.setFont("Helvetica-Bold", 14)

    p.drawString(
        80,
        460,
        "Thank you for booking with EventX!"
    )

    p.showPage()
    p.save()

    return response


# =========================
# REGISTER PAGE
# =========================

def register_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect(
                'register_page'
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully"
        )

        return redirect(
            'login_page'
        )

    return render(
        request,
        'register.html'
    )


# =========================
# LOGIN PAGE
# =========================

def login_page(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                'dashboard'
            )

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

            return redirect(
                'login_page'
            )

    return render(
        request,
        'login.html'
    )


# =========================
# LOGOUT
# =========================

def logout_page(request):

    logout(request)

    return redirect(
        'login_page'
    )


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    if not request.user.is_authenticated:

        return redirect(
            'login_page'
        )

    bookings = Booking.objects.filter(
        email=request.user.email
    ).order_by('-booking_date')

    context = {
        'bookings': bookings
    }

    return render(
        request,
        'dashboard.html',
        context
    )