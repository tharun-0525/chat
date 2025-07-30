from django.db import models
from myapp.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="message", null= True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add= True)
