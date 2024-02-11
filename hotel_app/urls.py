
from django.urls import path, include
from hotel_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('hotels', views.HotelViewSet)
router.register('hotel_details', views.HotelDetailsViewSet)
router.register('reviews', views.ReviewsAndRatingViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
