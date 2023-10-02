from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Booking by {self.first_name + ' ' + self.last_name}"
