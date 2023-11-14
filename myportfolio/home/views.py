from smtplib import SMTPException
from django.core.mail import EmailMessage
from django.shortcuts import render
from .models import Projects, ContactUs

import logging
from django.contrib import messages
logger = logging.getLogger(__name__)

def HomeView(request):
    project = Projects.objects.all()
    if request.method == 'POST':
        # Data Saving Function
        get_first_name = request.POST.get('firstname')
        get_last_name = request.POST.get('lastname')
        get_email = request.POST.get('email')
        get_subject = request.POST.get('subject')
        get_message = request.POST.get('message')

        try:
            # Email Sending Function
            email_subject = 'Contact Form Submission from {} {}'.format(get_first_name, get_last_name)
            email_message = EmailMessage(email_subject, get_message, 'farhanbasheerofficial10@gmail.com', ['farhanbasheerofficial10@gmail.com'], [], reply_to=[get_email,])
            email_message.send()
            print("Email Has Been Sent Successfully")

             # Save form data to the ContactUs model
            var_send_message = ContactUs(first_name=get_first_name, last_name=get_last_name, email=get_email, subject=get_subject, message_body=get_message)
            var_send_message.save()
            messages.success(request, "Form submitted successfully.")
            
        except (SMTPException, Exception) as e:
            logger.error(f"Error Occurred While Sending Email: {e}")
            messages.error(request, "An error occurred. Please try again later.")
    
    context = {'all_projects': project}
    return render(request, 'home/index.html', context)


def PortfolioDetailView(request, pk):
    Project_Detail = Projects.objects.get(id=pk)
    context = {'Project':Project_Detail}
    return render(request,'home/portfolio-details.html', context)
