from .models import Customer, Booking
from django import forms
from django.forms.widgets import DateInput


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number')

# https://stackoverflow.com/questions/61077802/how-to-use-a-datepicker-in-a-modelform-in-django


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'number_attending')
        widgets = {
            'booking_date': DateInput(attrs={'type': 'date'}),
        }
