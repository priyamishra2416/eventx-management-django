from django.urls import path

from .views import *



urlpatterns = [

    # =========================
    # HOME PAGE
    # =========================

    path(
        '',
        home,
        name='home'
    ),



    # =========================
    # EVENT DETAIL
    # =========================

    path(
        'event/<int:id>/',
        event_detail,
        name='event_detail'
    ),



    # =========================
    # BOOKING PAGE
    # =========================

    path(
        'booking/<int:id>/',
        booking_page,
        name='booking_page'
    ),



    # =========================
    # QR TICKET PAGE
    # =========================

    path(
        'ticket/<int:id>/',
        ticket_page,
        name='ticket_page'
    ),



    # =========================
    # PDF DOWNLOAD
    # =========================

    path(
        'download-ticket/<int:id>/',
        download_ticket,
        name='download_ticket'
    ),



    # =========================
    # AUTHENTICATION
    # =========================

    path(
        'register/',
        register_page,
        name='register_page'
    ),

    path(
        'login/',
        login_page,
        name='login_page'
    ),

    path(
        'logout/',
        logout_page,
        name='logout_page'
    ),



    # =========================
    # USER DASHBOARD
    # =========================

    path(
        'dashboard/',
        dashboard,
        name='dashboard'
    ),

]