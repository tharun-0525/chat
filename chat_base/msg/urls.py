from django.contrib import admin
from django.urls import path, include
from .views import text_view
from myapp.views import profile_view
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'msg'
urlpatterns = [
    path("",text_view,name= "screen"),
    path("logout/",LogoutView.as_view(next_page="myapp:login"),name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
