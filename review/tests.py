from django.test import TestCase
from .models import Review
from django.urls import reverse


class ReviewTestCase(TestCase):

    def setUp(self):
        """
        Set up method to mock a review being created
        """
        Review.objects.create(name="Mark", body="I loved visiting cafe-board",
                              stars='5', created_on='25/10/2023')

    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if the review url exists
        The following two resources helped with all tests in this project.
        https://docs.djangoproject.com/en/4.2/topics/testing/overview/
        https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if the review view is accessable by name.
        """
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if the review view uses the correct template.
        """
        response = self.client.get(reverse('review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class MenuTestCase(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if menu url exists.
        """
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if menu view is accessible by name.
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if menu view uses correct template.
        """
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')


class GamesTestCase(TestCase):

    def test_view_url_exists_at_desired_location(self):
        """
        Test to determine if games url exists.
        """
        response = self.client.get('/games')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test to determine if games view is accessible by name.
        """
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test to determine if games view uses correct template.
        """
        response = self.client.get(reverse('games'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games.html')
