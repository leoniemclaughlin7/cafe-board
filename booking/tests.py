from django.test import TestCase
from django.urls import reverse
from .models import Customer, Booking
from django.contrib.auth.models import User

# Create your tests here.


class CustomerBookingTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookings/booking')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')


# https://stackoverflow.com/questions/29946229/django-test-client-login-doesnt-work
class DisplayBookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", 
                                                password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Customer.objects.create(first_name="Mark", last_name="Itest",
                            email='mark@itest.com', phone_number='0123456',
                            user=self.user)
        customer = Customer.objects.get(first_name='Mark')
        Booking.objects.create(booking_date='2023-10-25', booking_time='10:00', 
                            number_attending='2', booking_status='1', 
                            customer=customer)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookings/display_booking')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('display_booking'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('display_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class EditBookingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Customer.objects.create(first_name="Mark", last_name="Itest",
                                email='mark@itest.com', phone_number='0123456', user=self.user)
        customer = Customer.objects.get(first_name='Mark')
        Booking.objects.create(booking_date='2023-10-25', booking_time='10:00',
                               number_attending='2', booking_status='1', customer=customer)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/bookings/edit_booking/1/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('edit_booking', kwargs={'booking_id':1, 'customer_id':1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/bookings/edit_booking/1/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')
