from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class User(AbstractUser):
    email = models.EmailField(default='example@example.com')
    pfp = models.ImageField(upload_to="profile_photo/", null=True, blank=True)
    plang = models.CharField(
        max_length=10,
        choices=[
            ('en', 'English'),
            ('es', 'Spanish'),
            ('fr', 'French'),
            ('de', 'German'),
            ('zh', 'Chinese'),
            ('ja', 'Japanese'),
            ('ru', 'Russian'),  
        ],
        default='en'
    )
    lmode = models.BooleanField(default=False)
