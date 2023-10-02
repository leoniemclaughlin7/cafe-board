from django.shortcuts import render
from .forms import CustomerBookingForm

# Create your views here.

def customer_booking(request):
    if request.method == 'POST':
        form = CustomerBookingForm(request.POST)
        if form.is_valid():


    else:
        form = CustomerBookingForm()

    context = {
        'form': form,
    }

    return render(request, 'booking.html', context)
