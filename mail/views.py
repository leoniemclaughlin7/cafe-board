from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.contrib import messages


def send_email(request):
    """
    Send email function connects the hosts details from settings.py
    and then set the details for the email to be sent to the host user.
    Assistance with django emails: https://opensource.com/article/22/12/django-send-emails-smtp
    A Success message is displayed once email is sent successfully.
    Help with EmailMessage class: https://stackoverflow.com/questions/59802624/contact-form-sending-emails-from-and-to-the-same-email-django 
    """
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
            EmailMessage(subject=name, body=message, from_email=from_email,
                         to=recipient_list, reply_to=[from_email], connection=connection).send()
        messages.add_message(request, messages.SUCCESS,
                             'Your message was sent. Please check your" \
                                "email for a reply in 24hrs.')
    return render(request, 'contact.html')
