from django.shortcuts import render
from rest_framework import viewsets
from hotel_app import models
from hotel_app.serializers import HotelSerializer, HotelDetailsSerializer, ReviewsAndRatingSerializer, ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend


class HotelViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = HotelDetailsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id',]


class ReviewsAndRatingViewSet(viewsets.ModelViewSet):
    queryset = models.ReviewsAndRating.objects.all()
    serializer_class = ReviewsAndRatingSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = models.Reservation.objects.all()
    serializer_class = ReservationSerializer
