import dataclasses
from django.shortcuts import render ,  get_object_or_404
from django.http import HttpResponse 
from django.core.mail import EmailMultiAlternatives
from asperdirect.settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail
# from django.core.mail import  send_mail
from django.core.mail import EmailMessage
from .models import Email
from django.core import mail

from django.http import JsonResponse
def email(request):
# fetch data
    if request.method == 'POST':
        
        # email = email(request.POST)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email= request.POST.getlist('email')
        # attach = request.FILES.getlist('attach')
        # def recipient(request):
        #  dataclasses(Email.objects.values())
        #  return JsonResponse(dataclasses,safe = False)

        print('subject',subject )
        print('message',message )
        print('email',email )
        # print('file',attach )

        # send_mass_mail((subject), (message), EMAIL_HOST_USER, email)


        msg = EmailMultiAlternatives((subject), (message), EMAIL_HOST_USER, email)
        # msg.attach( "{{attach}}" , content= '')
        msg.send()

    return render(request, 'email/email.html')


def template(request):
 if request.method == 'POST':
    email1= request.POST.get('email1')
    email2= request.POST.get('email2')
    email3= request.POST.get('email3')
    email4= request.POST.get('email4')
    email5= request.POST.get('email5')
    email6= request.POST.get('email6')

    message1 = ('subject1', 'this is an email 1 message' , EMAIL_HOST_USER , [email1])
    message2 = ('subject2', 'this is an email 2 message' , EMAIL_HOST_USER , [email2])
    message3 = ('subject3', 'this is an email 3 message' , EMAIL_HOST_USER , [email3])
    message4 = ('subject4', 'this is an email 4 message' , EMAIL_HOST_USER , [email4])
    message5 = ('subject5', 'this is an email 5 message' , EMAIL_HOST_USER , [email5])
    message6 = ('subject6', 'this is an email 6 message' , EMAIL_HOST_USER , [email6])




    send_mass_mail((message1, message2, message3 , message4, message5 , message6), fail_silently=False)
 return render(request, 'email/template.html')

