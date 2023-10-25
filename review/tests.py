from django.test import TestCase
from .models import Review
from django.urls import reverse

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
# Create your tests here.


class ReviewTestCase(TestCase):
    def setUp(self):
        Review.objects.create(name="Mark", body="I loved visiting cafe-board",
                              stars='5', created_on='25/10/2023')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
