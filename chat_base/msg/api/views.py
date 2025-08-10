from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer, MessageSerializer
from  msg.models import Message
from django.db.models import Q
from msg.utils import translateLang
from django.contrib.auth import get_user_model


class ScreenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        """Fetch chat history"""
        user1 = request.user.username
        user2 = username
        messages = Message.objects.filter(
            Q(sender__username=user1, reciever__username=user2) |
            Q(sender__username=user2, reciever__username=user1)
        ).order_by('time')

        for msg in messages:
            msg.translated_text = (
                translateLang(msg.text, request.user.plang)
                if request.user.lmode else msg.text
            )

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, username):
        User = get_user_model()
        """Send new message (validated via serializer)"""
        data = request.data.copy()  # copy to avoid messing with immutable QueryDict

        # Handle translation if lmode is enabled
        if request.user.lmode and data.get('text'):
            data['text'] = translateLang(data['text'], 'en')

        # Pre-fill sender & receiver since client doesn't need to send them
        data['sender'] = request.user.id
        data['reciever'] = User.objects.get(username=username).id

        serializer = MessageSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username):
        """Toggle language mode"""
        request.user.lmode = not request.user.lmode
        request.user.save()
        return Response({"lmode": request.user.lmode})