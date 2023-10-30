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
            from_email = request.POST.get("email")
            recipient_list = [settings.EMAIL_HOST_USER,]
            message = request.POST.get("message")
            EmailMessage(name, message, from_email,
                         recipient_list, connection=connection).send()
        messages.add_message(request, messages.SUCCESS,
                             'Your message was sent. Please check your" \
                                "email for a reply in 24hrs.')
    return render(request, 'contact.html')
