from django.contrib import admin
from .models import Customer, Booking

# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')


@admin.register(Booking)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer', 'booking_date', 'booking_time',
                    'number_attending', 'booking_status')
    list_filter = ('booking_status', 'booking_date')
