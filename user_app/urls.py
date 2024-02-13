
from django.urls import path
from user_app import views

urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view(), name="signup"),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLoginView.as_view(), name='logout')
]
