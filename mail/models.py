from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Email(models.Model):
     subject = models.CharField(max_length=50, default="")
     message = models.TextField(max_length=500, default="")
     email = models.CharField(max_length=1000, default="")
     attach = models.FileField(default='', upload_to='doc', blank='')

     
