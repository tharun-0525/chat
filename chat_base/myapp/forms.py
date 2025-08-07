from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",  "email", "password1", "password2", "plang")
         

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pfp', 'plang']