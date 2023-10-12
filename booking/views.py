from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, BookingForm
from django.contrib.auth.models import User
from .models import Booking, Customer
from django.db.models import Sum
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


# Create your views here.
# https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query


def check_availability(date, time):
    all_bookings = Booking.objects.all()
    unavailable = Booking.objects.filter(
        booking_date=date, booking_time=time)
    available = True
    total_attendees = unavailable.aggregate(Sum('number_attending'))[
        'number_attending__sum']
    for booking in all_bookings:
        if unavailable.exists() and total_attendees > 20:
            available = False
        else:
            available = True
    return available


def limit_no_attendees(date, time, attending):
    attendees_limit = False
    unavailable = Booking.objects.filter(
        booking_date=date, booking_time=time)
    total_attendees = unavailable.aggregate(Sum('number_attending'))[
        'number_attending__sum']

    if total_attendees is None:
        total_attendees = 0
    if total_attendees + attending <= 20:
        attendees_limit = True
    else:
        attendees_limit = False
    return attendees_limit


def unavailable_dates():
    confirmed_bookings = Booking.objects.filter(booking_status=1)
    bookings_max_attendees = confirmed_bookings.values(
        'booking_date', 'booking_time').annotate(
            attendees=Sum('number_attending')).filter(attendees=20)
    unavailable_dates = [booking['booking_date'] for booking in bookings_max_attendees]
    dataJSON = json.dumps(unavailable_dates, cls=DjangoJSONEncoder)
    return dataJSON
   

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
            if limit_no_attendees(booking.booking_date, booking.booking_time, booking.number_attending):
                booking.save()
                customer_form = CustomerForm()
                booking_form = BookingForm()
                messages.add_message(request, messages.SUCCESS,
                                     'Your booking request was successful, please visit your profile to view the status!')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Date and time unavailable!')

    else:
        customer_form = CustomerForm(prefix='customer')
        booking_form = BookingForm(prefix='booking')
        unavailable_booking_dates = unavailable_dates()
        print(unavailable_booking_dates)
        

    context = {
        'customer_form': customer_form,
        'booking_form': booking_form,
        'unavailable_dates': unavailable_booking_dates,
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


def edit_booking(request, booking_id, customer_id):
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        booking_form = BookingForm(request.POST, instance=booking)
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid() and booking_form.is_valid():
            booking_form.save()
            customer_form.save()
            return redirect('display_booking')
    booking_form = BookingForm(instance=booking)
    customer_form = CustomerForm(instance=customer)
    context = {
        'booking_form': booking_form,
        'customer_form': customer_form
    }
    return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id, customer_id):
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    booking.delete()
    customer.delete()
    return redirect('display_booking')
