from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

# Create your views here.


def send_email(request):
    if request.method == "POST":
        with get_connection(
           host=settings.EMAIL_HOST,
           port=settings.EMAIL_PORT,
           username=settings.EMAIL_HOST_USER,
           password=settings.EMAIL_HOST_PASSWORD,
           use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            name = request.POST.get("name")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST.get("email"), ]
            message = request.POST.get("message")
            EmailMessage(name, message, email_from,
                         recipient_list, connection=connection).send()

    return render(request, 'contact.html')
