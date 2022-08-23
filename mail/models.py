from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Email(models.Model):
     subject = models.CharField(max_length=50)
     message = models.TextField(max_length=500)
     email = models.CharField(max_length=1000)

   #   def __str__(self):
   #      return self.email

   #   def get_absolute_url(self):
   #      return reverse('email/email.html', kwargs={'pk': self.pk})