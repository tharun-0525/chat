from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Message, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.db.models import Q
from .utils import translateLang
from django.contrib.auth import get_user_model
change =1

@ login_required
def screen_view(request):
    users = User.objects.all()
    return render(request, 'msg/screen.html', {'users': users})

@login_required
def text_view(request, username):
    if request.method == 'POST':
        print("POST request received")
        form_type = request.POST.get('form_type')

        if form_type == 'send_message':
            print("Sending message")
            content = request.POST.get('text')
            if content:
                user = request.user
                Message.objects.create(
                    sender=user,
                    reciever=User.objects.get(username=username),
                    text=content
                )
            return redirect('msg:text', username=username)
        elif form_type == 'toggle':
            request.user.lmode = not request.user.lmode
            request.user.save()
            return redirect('msg:text', username=username)
    user1 = request.user.username
    user2 = username
    messages = Message.objects.filter(
        Q(sender__username=user1, reciever__username=user2) |
        Q(sender__username=user2, reciever__username=user1)
    ).order_by('time')

    if request.user.lmode == True:
        print("Translating messages")
        for msg in messages:
            msg.translated_text = translateLang(msg.text, request.user.plang)
    else:
        print("No translation needed")
        for msg in messages:
            msg.translated_text = msg.text
    
    return render(request, 'msg/messages.html', {
        'messages': messages,
        'reciever': User.objects.get(username=username)
    })

