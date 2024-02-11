from django.db import models
from .constants import HOTEL_TYPES, HOTEL_RESERVATION_STATUS, HOTEL_ROOM_TYPES
from user_app.models import User


def hotel_image_upload(instance, filename):
    return f"hotel/{instance.name}/main/{filename}"


def room_image_upload(instance, filename):
    return f"hotel/{instance.hotel.name}/room/{filename}"


def amenity_image_upload(instance, filename):
    return f"amenity/{instance.name}/{filename}"


def pakage_image_upload(instance, filename):
    return f"pakage/{instance.name}/{filename}"


class Amenity(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to=amenity_image_upload, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    hotel_rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to=hotel_image_upload, blank=True)
    amenities = models.ManyToManyField(Amenity)
    hotel_type = models.CharField(choices=HOTEL_TYPES, max_length=5)

    def __str__(self) -> str:
        return f"{self.name}"


class HotelRoom(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='hotel_rooms')
    room_type = models.CharField(choices=HOTEL_ROOM_TYPES, max_length=10)
    image = models.ImageField(upload_to=room_image_upload, blank=True)
    capacity = models.IntegerField(default=0)
    price_per_day = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f"{self.hotel.name}'s room"


# class Pakage(models.Model):
#     name = models.CharField(max_length=55)
#     description = models.CharField(max_length=400)
#     price = models.DecimalField(decimal_places=2, max_digits=12)
#     image = models.ImageField(upload_to=pakage_image_upload, blank=True)

#     def __str__(self) -> str:
#         return f"{self.name}"


class Reservation(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_reservations')
    hotel_room = models.ForeignKey(
        HotelRoom, on_delete=models.CASCADE, related_name='room_reservations')
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    room_type = models.CharField(choices=HOTEL_ROOM_TYPES, max_length=10)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    total_day = models.IntegerField(default=1)
    status = models.CharField(choices=HOTEL_RESERVATION_STATUS, max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.guest.first_name} {self.guest.first_name}'s reservations"


class ReviewsAndRating(models.Model):
    hotel = models.ForeignKey(
        Hotel, on_delete=models.CASCADE, related_name='hotel_reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_reviews')
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name='reservation_reviews')
    review = models.CharField(max_length=300)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.hotel.name}'s reviews"
