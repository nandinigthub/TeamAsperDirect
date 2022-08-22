from django.shortcuts import render
# from django.core.mail import EmailMultiAlternatives
from asperdirect.settings import EMAIL_HOST_USER
from django.core.mail import BadHeaderError, send_mass_mail
from .models import Email
def email(request):
    # template
    message1 = ('termination mail', 'Dear abc, It is our unfortunate duty to inform you that your employment with (add company name) stands terminated from (add date).The reason for termination is the multiple unexplained and uninformed leave of absence from work for prolonged periods that you have taken.You will receive your entitled severance package as per company policy. You will receive a statement detailing your accrued benefits.(Name of HR executive) will discuss the final details with you as well as answer your question or doubts, if any. Kindly get in touch with him/her at the earliest to discuss your termination process and final package.This action by us was deemed necessary. We wish you success in your future endeavours.', EMAIL_HOST_USER, ['gattanilalita@gmail.com','brijeshgattani@gmail.com','gattaninandini02@gmail.com'])
    message2 = ('job acceptance', 'Here is another testing message part2 ', EMAIL_HOST_USER, ['archita465@gmail.com' , 'gattaninandini02@gmail.com'])
    message3 = ('resign', 'Here is another testing message part2 ', EMAIL_HOST_USER, ['archita465@gmail.com' , 'gattaninandini02@gmail.com'])
    send_mass_mail((message1, message2, message3), fail_silently=False)

# fetch data
    # if request.method == 'POST':
    #     subject = request.POST.get('subject')
    #     message = request.POST.get('message')
    #     email= request.POST.get('email')

    #     new_mail = email(subject={"subject"}, message={"message"},email={"email"})
    #     new_mail.save()
    #     send_mass_mail((new_mail), fail_silently=False)

    return render(request, 'email/email.html')


# class EmailCreateView(LoginRequiredMixin, CreateView):
#     model = email
#     fields = ['subject', 'body']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)