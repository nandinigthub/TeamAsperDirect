from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Email(models.Model):
     subject = models.CharField(max_length=50)
     message = models.TextField(max_length=500)
     email = models.EmailField()

