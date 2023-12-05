from django.test import TestCase
from django.urls import reverse


class MailTestCase(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if the mail url exists
        """
        response = self.client.get('/contact/mail')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the mail view is accessable by name.
        """
        response = self.client.get(reverse('mail'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the mail view uses the correct template.
        """
        response = self.client.get(reverse('mail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
