from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import logging


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_login_view(self):
        # Test login with valid credentials
        # response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword', 'current_page': '/login'})
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json(), {'200': 'ok'})

        # Test login with invalid credentials
        response = self.client.post(
            self.login_url,
            {
                "username": "wronguser",
                "password": "wrongpassword",
                "current_page": "/login",
            },
        )
        logging.info(response)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"401": "pas ok"})

    def test_logout_view(self):
        # Login the user before testing logout
        self.client.login(username="testuser", password="testpassword")

        # Test logout
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Redirects after logout

        # Verify that the user is logged out
        response = self.client.get("/")
        self.assertEqual(
            response.status_code, 200
        )  # Assuming '/' is your homepage
        self.assertNotIn("_auth_user_id", self.client.session)
