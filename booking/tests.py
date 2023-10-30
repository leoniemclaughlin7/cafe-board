from django.test import TestCase
from django.urls import reverse
from .models import Customer, Booking
from django.contrib.auth.models import User


class CustomerBookingTestCase(TestCase):
    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if the booking url exists
        """
        response = self.client.get('/bookings/booking')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the booking view is accessable by name.
        """
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the booking view uses the correct template. 
        """
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')


class DisplayBookingTestCase(TestCase):
    def setUp(self):
        """
        Set up function creates a user and logs this user in to the site.
        It also sets up a test customer and booking. Assistance with logging 
        the user in for testing purposes was obtained here:
        https://stackoverflow.com/questions/29946229/django-test-client-login-doesnt-work
        """

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
        """
        Test to determine if the display_booking url exists
        """
        response = self.client.get('/bookings/display_booking')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the display_booking view is accessable by name.
        """
        response = self.client.get(reverse('display_booking'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the display_booking view uses the correct template. 
        """
        response = self.client.get(reverse('display_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class EditBookingTestCase(TestCase):
    def setUp(self):
        """
        Set up function creates a user and logs this user in to the site.
        It also sets up a test customer and booking.
        """
        self.user = User.objects.create_user(
            username="testuser", password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Customer.objects.create(first_name="Mark", last_name="Itest",
                                email='mark@itest.com', phone_number='0123456', user=self.user)
        customer = Customer.objects.get(first_name='Mark')
        Booking.objects.create(booking_date='2023-10-25', booking_time='10:00',
                               number_attending='2', booking_status='1', customer=customer)

    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if the edit_booking url exists it takes two
        endpoints booking_id and customer_id. 
        """
        response = self.client.get('/bookings/edit_booking/1/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the edit_booking view is accessable by name.
        It takes two arguments booking_id and customer_id. 
        """
        response = self.client.get(reverse('edit_booking', kwargs={'booking_id':1, 'customer_id':1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the edit_booking view uses the correct template.
        """
        response = self.client.get('/bookings/edit_booking/1/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_booking.html')


# https://stackoverflow.com/questions/71919799/assertionerror-302-200-couldnt-retrieve-redirection-page-api-v2-app-nex
class DeleteBookingTestCase(TestCase):
    def setUp(self):
        """
        Set up function creates a user and logs this user in to the site.
        It also sets up a test customer and booking.
        """
        self.user = User.objects.create_user(
            username="testuser", password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Customer.objects.create(first_name="Mark", last_name="Itest",
                                email='mark@itest.com', phone_number='0123456', user=self.user)
        customer = Customer.objects.get(first_name='Mark')
        Booking.objects.create(booking_date='2023-10-25', booking_time='10:00',
                               number_attending='2', booking_status='1', customer=customer)

    def test_view_url_exists_at_desired_location(self):
        """
        Test to see if delete booking url exists and that you are redirected
        to display_bookings once complete. 
        """
        response = self.client.get('/bookings/delete_booking/1/1')
        self.assertRedirects(response, '/bookings/display_booking',
                             target_status_code=200)

    def test_view_url_accessible_by_name(self):
        """
        Test to assess if delete_booking is accessible by name and that
        once comeplete it redirects to display_booking.
        """
        response = self.client.get(reverse('delete_booking', kwargs={
                                   'booking_id': 1, 'customer_id': 1}))
        self.assertRedirects(response, '/bookings/display_booking',
                             target_status_code=200)


class EditUserTestCase(TestCase):
    def setUp(self):
        """
        Set up function creates a user and logs this user in.
        """
        self.user = User.objects.create_user(
            username="testuser", password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_view_url_exists_at_desired_location(self):
        """
        Tests to determine if edit user url exists.
        """
        response = self.client.get('/bookings/edit_user/1')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the edit_user view is accessable by name.
        """
        response = self.client.get(reverse('edit_user', kwargs={
                                   'user_id': 1, }))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the edit_user view uses the correct template.
        """
        response = self.client.get('/bookings/edit_user/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_user.html')


class DeleteUserTestCase(TestCase):
    def setUp(self):
        """
        Set up function creates a user and logs this user in.
        """
        self.user = User.objects.create_user(
            username="testuser", password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_view_url_exists_at_desired_location(self):
        """
        Test to see if delete user url exists and that you are redirected
        to home page once complete.
        """
        response = self.client.get('/bookings/delete_user/1')
        self.assertRedirects(response, '/',
                             target_status_code=200)

    def test_view_url_accessible_by_name(self):
        """
        Test to assess if delete_user is accessible by name and that
        once comeplete it redirects to home page.
        """
        response = self.client.get(reverse('delete_user', kwargs={
                                   'user_id': 1 ,}))
        self.assertRedirects(response, '/',
                             target_status_code=200)
