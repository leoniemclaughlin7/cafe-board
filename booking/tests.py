from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class BookingTestCase(TestCase):
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
