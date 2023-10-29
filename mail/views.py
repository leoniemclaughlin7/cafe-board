from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib import messages

# Create your views here.

# https://opensource.com/article/22/12/django-send-emails-smtp


def send_email(request):
    if request.method == "POST":
        with get_connection(
           host=settings.EMAIL_HOST,
           port=settings.EMAIL_PORT,
           username=settings.EMAIL_HOST_USER,
           password=settings.EMAIL_HOST_PASS,
           use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            name = request.POST.get("name")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")
            EmailMessage(name, message, email_from,
                         recipient_list, connection=connection).send()
        messages.add_message(request, messages.SUCCESS,
                             'Your message was sent. Please check your email for a reply.')
         
    return render(request, 'contact.html')
