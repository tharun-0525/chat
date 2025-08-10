from rest_framework import serializers
from django.contrib.auth import get_user_model
from msg.models import Message
from msg.utils import translateLang

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username']

class MessageSerializer(serializers.ModelSerializer):
    translated_text = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'reciever', 'text', 'time', 'translated_text']
        

    def get_translated_text(self, obj):
        request = self.context.get('request')
        if request and getattr(request.user, 'lmode', False):
            return translateLang(obj.text, request.user.plang)
        return obj.text
