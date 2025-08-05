from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Message, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.db.models import Q

@ login_required
def screen_view(request):
    users = User.objects.all()
    return render(request, 'msg/screen.html', {'users': users})

@login_required
def text_view(request, username):
    if request.method=='POST':
        content = request.POST.get('text')
        if content:
            user=get_user(request)
            Message.objects.create(sender=user,reciever = User.objects.get(username=username),text=content)
        return redirect('msg:text', username=username)
    user1 = get_user(request).username
    user2 = username
    messages = Message.objects.filter(
        Q(sender__username=user1, reciever__username=user2) |
        Q(sender__username=user2, reciever__username=user1)
    ).order_by('time')
    return render(request, 'msg/messages.html', {'messages':messages,'reciever': User.objects.get(username=username)})
