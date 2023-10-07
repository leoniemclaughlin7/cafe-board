from django.shortcuts import render, get_object_or_404
from .forms import CustomerForm, BookingForm
from django.contrib.auth.models import User
from .models import Booking, Customer


# Create your views here.

# https://stackoverflow.com/questions/77218397/how-to-access-instances-of-models-in-view-in-order-to-save-both-forms-at-once?noredirect=1&lq=1
def customer_booking(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, prefix='customer')
        booking_form = BookingForm(request.POST, prefix='booking')
        if customer_form.is_valid() and booking_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.user = request.user
            customer.save()
            booking = booking_form.save(commit=False)
            booking.customer = customer
            booking.save()
            customer_form = CustomerForm()
            booking_form = BookingForm()

    else:
        customer_form = CustomerForm(prefix='customer')
        booking_form = BookingForm(prefix='booking')

    context = {
        'customer_form': customer_form,
        'booking_form': booking_form,
    }

    return render(request, 'booking.html', context)

# https://www.w3schools.com/django/django_queryset_filter.php


def display_booking(request):
    customer = Customer.objects.filter(user=request.user)
    bookings = Booking.objects.filter(customer__in=customer)
    context = {
        'bookings': bookings,
    }
    return render(request, 'profile.html', context)
