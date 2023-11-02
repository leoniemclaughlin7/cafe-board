from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import CustomerForm, BookingForm, UserForm
from django.contrib.auth.models import User
from .models import Booking, Customer
from django.db.models import Sum
from django.contrib import messages


def limit_no_attendees(date, time, attending):
    """
    Function checks if user is trying to book more than 20 places.
    It takes into consideration the already confirmed bookings for 
    specified date and will return false if the total number exceeds 20.
    Assistance of finding the sum of the number of attendees column was obtained
    here: https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query 
    """
    attendees_limit = False
    unavailable = Booking.objects.filter(booking_status=1,
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
    """
    Unavailable dates function takes into consideration if the cafe is 
    fully booked with confirmed bookings on a given date. This information is then passed to JS
    to block out dates that are unavailable. Assistance with the use of 
    annotate: https://stackoverflow.com/questions/60249631/how-to-use-django-annotate 
    """
    confirmed_bookings = Booking.objects.filter(booking_status=1)
    bookings_max_attendees = confirmed_bookings.values(
        'booking_date').annotate(
            attendees=Sum('number_attending')).filter(attendees=280)
    unavailable_dates = [booking['booking_date']
                         for booking in bookings_max_attendees]
    return unavailable_dates


def check_availability(date, time):
    """
    Check availability returns true if there is availability on a given date/time
    and false if the date or time is fully booked with confirmed bookings. 
    """
    unavailable = Booking.objects.filter(
        booking_date=date, booking_time=time, booking_status=1)
    available = True
    total_attendees = unavailable.aggregate(Sum('number_attending'))[
        'number_attending__sum']
    if unavailable.exists() and total_attendees >= 20:
        available = False
    else:
        available = True
    return available


def customer_booking(request):
    """
    Customer booking function renders the booking form with booking details and
    customer details. It checks that both check availability and limit no attendees
    returns true before allowing a booking to be made. Assistance with saving two forms 
    came from: https://stackoverflow.com/questions/77218397/how-to-access-instances-of-models-in-view-in-order-to-save-both-forms-at-once?noredirect=1&lq=1 
    """
    unavailable_booking_dates = []
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, prefix='customer')
        booking_form = BookingForm(request.POST, prefix='booking')
        if customer_form.is_valid() and booking_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.user = request.user
            customer.save()
            booking = booking_form.save(commit=False)
            booking.customer = customer
            if check_availability(booking.booking_date, booking.booking_time) and limit_no_attendees(booking.booking_date, booking.booking_time, booking.number_attending):
                booking.save()
                customer_form = CustomerForm()
                booking_form = BookingForm()
                messages.add_message(request, messages.SUCCESS,
                                     'Your booking request was successful, please see status below!')
                return redirect('display_booking')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Date and time unavailable!')
    else:
        customer_form = CustomerForm(prefix='customer')
        booking_form = BookingForm(prefix='booking')
        unavailable_booking_dates = unavailable_dates()

    context = {
        'customer_form': customer_form,
        'booking_form': booking_form,
        'unavailable_dates': unavailable_booking_dates,
    }

    return render(request, 'booking.html', context)


def display_booking(request):
    """
    Display booking shows the user their bookings on 
    the profile page. Assistance with the queryset filter
    came from: https://www.w3schools.com/django/django_queryset_filter.php
    """
    customer = Customer.objects.filter(user=request.user)
    bookings = Booking.objects.filter(customer__in=customer)
    context = {
        'bookings': bookings,
    }
    return render(request, 'profile.html', context)


def edit_booking(request, booking_id, customer_id):
    """
    Edit booking function will display a pre filled form for a 
    specific booking of the users choosing and allows this booking to be edited.
    Help with securing the url:
    https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_
    """
    unavailable_booking_dates = []
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    if not customer.user == request.user:
        messages.error(request, 
        'Error, you are unauthorised to edit this booking')
        return redirect(reverse('display_booking'))
    else:
        if request.method == "POST":
            booking_form = BookingForm(request.POST, instance=booking)
            customer_form = CustomerForm(request.POST, instance=customer)
            if customer_form.is_valid() and booking_form.is_valid():
                booking_form.save()
                customer_form.save()
                return redirect('display_booking')
        booking_form = BookingForm(instance=booking)
        customer_form = CustomerForm(instance=customer)
        unavailable_booking_dates = unavailable_dates()
        context = {
            'booking_form': booking_form,
            'customer_form': customer_form,
            'unavailable_dates': unavailable_booking_dates,
        }
        return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id, customer_id):
    """
    Delete booking will delete a specific booking of a users choosing.
    A message is displayed to user once booking has been deleted.
    This function redirects to display booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    booking.delete()
    customer.delete()
    messages.add_message(request, messages.WARNING,
                         'Booking has been deleted!')
    return redirect('display_booking')


def edit_user(request, user_id):
    """
    Edit user allows the user to edit their username and email.
    """
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('display_booking')
    form = UserForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'edit_user.html', context)


def delete_user(request, user_id):
    """
    Delete user will delete a users account. A message is displayed to the user 
    if deletion is successfull.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.add_message(request, messages.WARNING,
                         'User account has been deleted!')
    return redirect('review')
