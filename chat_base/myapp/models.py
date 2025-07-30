from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class User(AbstractUser):
    email = models.EmailField(default='example@example.com')
    pfp = models.ImageField(upload_to="profile_photo/", null=True, blank=True)

