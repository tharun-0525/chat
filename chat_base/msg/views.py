from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Message, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

# Create your views here.
# class thread(ListView):
#     model= Message
#     template_name = 'msg/screen.html'
#     context_object_name = 'messages'
#     ordering = ['time']

@login_required
def text_view(request):
    if request.method=='POST':
        content = request.POST.get('text')
        print("content recieved")
        if content:
            user=get_user(request)
            print(user)
            Message.objects.create(user=user,text=content)
            print("content saved")
        return redirect('msg:screen')
    
    messages = Message.objects.order_by('time')
    return render(request, 'msg/screen.html', {'messages':messages})
