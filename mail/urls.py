from django.urls import path,include
from . import views

urlpatterns = [
    path('email/',views.email,name='email')
]
