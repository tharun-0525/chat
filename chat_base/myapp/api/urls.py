from django.urls import path
from .views import RegisterAPIView, ProfileAPIView, ProfileEditAPIView


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/<str:username>/', ProfileAPIView.as_view(), name='profile'),
    path('profile/edit/', ProfileEditAPIView.as_view(), name='profile_edit'),
]
