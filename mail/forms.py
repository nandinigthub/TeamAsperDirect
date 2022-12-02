from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Email

class AttachementForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['attach']