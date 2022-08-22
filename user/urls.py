from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views

urlpatterns = [
    path('home/', views.home,name='user-home'),
    path('dept/', views.dept,name='user-dept'),
    # path('profile/' ,views.profile,name='user-profile'), 
    # path('reset/' ,views.reset,name='user-reset'), 
    # path('reset/' ,views.reset,name='user-reset'), 
]