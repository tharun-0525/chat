from django.contrib import admin
from django.urls import path, include
from .views import text_view, screen_view, text_send, text_toggle
from myapp.views import profile_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .api.views import ScreenView

app_name = 'msg'
urlpatterns = [
    path("", screen_view, name="screen"),
    path("<str:username>/",text_view,name= "text"),
    path("<str:username>/send/", text_send, name="text_send"),
    path("<str:username>/toggle/", text_toggle, name="text_toggle"),
    path("logout/",LogoutView.as_view(next_page="myapp:login"),name="logout"),
    path("api/", include("msg.api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
