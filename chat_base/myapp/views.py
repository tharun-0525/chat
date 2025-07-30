from django.shortcuts import render
from .models import User
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
# Create your views here.

class register_view(CreateView):
    form_class = CustomUserCreationForm
    template_name= "myapp/register.html"
    success_url = reverse_lazy("myapp:login")

class profile_view(LoginRequiredMixin,DetailView):
    model = User
    template_name = "myapp/profile.html"
    context_object_name = "profile_user"

    def get_object(self, queryset =None):
        username = self.kwargs.get('username')
        if username:
            return get_object_or_404(User, username=username)
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_own_profile'] = self.object == self.request.user
        return context 


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'myapp/pchange.html'
    
    def get_success_url(self):
        return reverse("myapp:profile", kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user

    








