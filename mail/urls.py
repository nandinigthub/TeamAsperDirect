from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('email/',views.email,name='email'),
    path('template/',views.template,name='template'),
    # path("",views.jsondata,name = "jsondata"),

]
