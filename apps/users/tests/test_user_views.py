from django.core.paginator import Paginator
from django.test import Client, TestCase
from django.urls import reverse
from apps.users.models import User

class UserViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="testuser@gmail.com",
            username="testuser",
            first_name="Test",
            last_name="User",
            phone_number="07456787878",
            gender="Male",
            id_number="87387878799",
            address="228-90119",
            city="Nairobi",
            country="Kenya"
        )

        self.user.set_password("1234")
        self.user.save()
   

    def test_user_login(self):
        data = {
            "username": self.user.username,
            "password": "1234"
        }

        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.logout()
        self.assertEqual(response, None)
        