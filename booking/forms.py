from .models import Customer, Booking, User
from django import forms
from django.forms.widgets import DateInput, TimeInput


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone_number')


# https://stackoverflow.com/questions/61077802/how-to-use-a-datepicker-in-a-modelform-in-django
# https://stackoverflow.com/questions/2580955/disable-autocomplete-on-textfield-in-django
# https://jqueryui.com/datepicker/


class BookingForm(forms.ModelForm):
    """
    Booking form set up. It includes the widgets for the
    datepicker and timepicker. Autocomplete is also turned
    off for these fields.
    """
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'number_attending')
        widgets = {
            'booking_date': DateInput(attrs={'id': 'datepicker',
                                             'autocomplete': 'off'}),
            'booking_time': TimeInput(attrs={'id': 'timepicker',
                                             'autocomplete': 'off'})
        }


class UserForm(forms.ModelForm):
    """
    User form set up.
    """
    class Meta:
        model = User
        fields = ('username', 'email')
