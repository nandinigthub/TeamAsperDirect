from django.shortcuts import render ,  get_object_or_404
from django.http import HttpResponse 
from django.core.mail import EmailMultiAlternatives
from asperdirect.settings import EMAIL_HOST_USER
from django.core.mail import BadHeaderError, send_mass_mail
from django.core.mail import  send_mail
from django.core.mail import EmailMessage
from .models import Email
from django.core import mail
def email(request):
# fetch data
    if request.method == 'POST':
        # email = email(request.POST)
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email= request.POST.get('email')
        attach = request.FILES.getlist('attach')

        # print('subject',subject )
        # print('message',message )
        # print('email',email )
        # print('html code',html_content)

        msg = EmailMultiAlternatives((subject), (message), EMAIL_HOST_USER, [email])
        msg.attach(attach.)
        msg.send()

    return render(request, 'email/email.html')



def template(request):
 if request.method == 'POST':
    email1= request.POST.get('email1')
    email2= request.POST.get('email2')
    email3= request.POST.get('email3')
    email4= request.POST.get('email4')
    email5= request.POST.get('email5')

    message1 = ('subject1', 'this is an email 1 message' , EMAIL_HOST_USER , [email1])
    message2 = ('subject2', 'this is an email 2 message' , EMAIL_HOST_USER , [email2])
    message3 = ('subject3', 'this is an email 3 message' , EMAIL_HOST_USER , [email3])
    message4 = ('subject4', 'this is an email 4 message' , EMAIL_HOST_USER , [email4])
    message5 = ('subject5', 'this is an email 5 message' , EMAIL_HOST_USER , [email5])




    send_mass_mail((message1, message2, message3 , message4, message5), fail_silently=False)
 return render(request, 'email/template.html')

