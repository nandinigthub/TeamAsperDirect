
from django.shortcuts import render
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def recipient(request):
     email = ArrayField(models.CharField(max_length=50), default=(),blank=True)
     arr = [10,22,33,45]
     email['arr'] = arr
     return email
#     arr=[]
    
#     for i in arr:
#      arr =  arr + arr[i] + ","

 

# return render 'nandini'
 
class Email(models.Model):
     subject = models.CharField(max_length=50, default="")
     message = models.TextField(max_length=500, default="")
     email = models.EmailField(max_length=50, default="")
     # def recipient(request):
     #     arr = [] 
     #     for i in arr:
     #      arr =  arr + arr[i] + "," 

     #     return arr
     # attach = models.FileField(default='', upload_to='doc', blank='')

     
