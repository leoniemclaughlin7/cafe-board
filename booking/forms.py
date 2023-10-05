from .models import Customer, Booking
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'number_attending')


