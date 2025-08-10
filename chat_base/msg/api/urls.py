from django.urls import path
from .views import ScreenView, ChatView

urlpatterns = [
    path('screen/', ScreenView.as_view(), name='screen'),
    path('chat/<str:username>/', ChatView.as_view(), name='chat'),
]

