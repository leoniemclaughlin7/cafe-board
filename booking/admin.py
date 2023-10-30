from django.contrib import admin
from .models import Customer, Booking

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customer admin set up, using list display to change
    the layout of the customer table.
    """
    list_display = ('first_name', 'last_name', 'email', 'phone_number')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Booking admin set up, using list display to change
    the layout of the booking table and list filter so as admin
    can filter the bookings by status and date.
    """
    list_display = ('customer', 'booking_date', 'booking_time',
                    'number_attending', 'booking_status')
    list_filter = ('booking_status', 'booking_date')
