from django.db import models
from myapp.models import User
from chat.settings import AUTH_USER_MODEL

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="user1", null= True)
    reciever = models.ForeignKey(AUTH_USER_MODEL, on_delete= models.CASCADE, related_name="user2", null= True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add= True)
