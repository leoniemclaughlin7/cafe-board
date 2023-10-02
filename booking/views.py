from django.shortcuts import render
from .forms import CustomerBookingForm

# Create your views here.


def customer_booking(request):
    if request.method == 'POST':
        customer_booking_form = CustomerBookingForm(request.POST)
        # if form.is_valid():
        #     form.save()

    else:
        customer_booking_form = CustomerBookingForm()

    context = {
        'form': customer_booking_form,
    }

    return render(request, 'booking.html', context)
