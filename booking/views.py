from django.shortcuts import render
from .forms import CustomerForm, BookingForm


# Create your views here.

# https://stackoverflow.com/questions/77218397/how-to-access-instances-of-models-in-view-in-order-to-save-both-forms-at-once?noredirect=1&lq=1
def customer_booking(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, prefix='customer')
        booking_form = BookingForm(request.POST, prefix='booking')
        if customer_form.is_valid() and booking_form.is_valid():
            customer_instance = customer_form.save()
            booking_instance = booking_form.save(commit=False)
            booking_instance.customer = customer_instance
            booking_instance.save()
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
