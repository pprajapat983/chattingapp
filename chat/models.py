from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    msg=models.CharField(max_length=400)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} message'