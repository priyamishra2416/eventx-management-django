from django.db import models

import uuid



# =========================
# EVENT MODEL
# =========================

class Event(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='events/')

    date = models.DateField()

    location = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    total_seats = models.IntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):

        return self.title




# =========================
# BOOKING MODEL
# =========================

class Booking(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    seats = models.IntegerField(default=1)

    booking_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    qr_code = models.ImageField(
        upload_to='qr_codes/',
        blank=True,
        null=True
    )

    booking_date = models.DateTimeField(
        auto_now_add=True
    )



    def __str__(self):

        return self.full_name