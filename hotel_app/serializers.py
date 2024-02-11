from rest_framework import serializers
from rest_framework import viewsets
from hotel_app import models


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amenity
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = "__all__"


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoom
        fields = "__all__"


class ReviewsAndRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewsAndRating
        fields = "__all__"


class HotelDetailsSerializer(serializers.ModelSerializer):
    amenities = AmenitiesSerializer(many=True, read_only=True)
    hotel_rooms = HotelRoomSerializer(many=True, read_only=True)
    hotel_reviews = ReviewsAndRatingSerializer(many=True, read_only=True)

    class Meta:
        model = models.Hotel
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = "__all__"
