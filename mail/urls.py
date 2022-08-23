from django.urls import path,include
from . import views

urlpatterns = [
    path('email/',views.email,name='email'),
    path('template/',views.template,name='template')

    # +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
