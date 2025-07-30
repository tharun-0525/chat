from django.urls import path
from . import views
from .views import register_view, profile_view, ProfileEditView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"
urlpatterns =[
    path("", register_view.as_view(), name= "register"),
    path("login/", LoginView.as_view(template_name="myapp/login.html"), name= "login"),
    path("logout/", LogoutView.as_view(next_page="myapp:login"), name= "logout"),
    path("profile/<str:username>/", profile_view.as_view(), name="profile"),
    path("profile/", profile_view.as_view(), name="profile"),
    path("profile/edit", ProfileEditView.as_view(), name='profile_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)