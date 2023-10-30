from django.db import models
from django.contrib.auth.models import User


BOOKING_STATUS = ((0, 'To be confirmed'), (1, 'Confirmed'), (2, 'Declined'))


class Customer(models.Model):
    """
    Customer model. Foregin key present to User.
    """
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}"


class Booking(models.Model):
    """
    Booking model. Foreign key present to Customer model
    """
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_attending = models.IntegerField(default=2)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking by {self.customer}"
