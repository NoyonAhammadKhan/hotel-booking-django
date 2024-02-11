from django.contrib import admin
from hotel_app.models import Hotel, HotelRoom, Reservation,  Amenity, ReviewsAndRating
# Register your models here.
admin.site.register(Amenity)
admin.site.register(Hotel)
admin.site.register(HotelRoom)
admin.site.register(Reservation)
admin.site.register(ReviewsAndRating)
