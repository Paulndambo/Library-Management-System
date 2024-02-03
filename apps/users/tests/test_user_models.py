from django.test import TestCase
from apps.users.models import User

class UserModelsTestCase(TestCase):
    def test_user_can_be_created(self):
        user = User.objects.create(
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

        user.set_password("1234")
        user.save()

        self.assertEqual(str(user), "testuser")

        return user

    def test_user_data_types(self):
        user = self.test_user_can_be_created()

        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.username, str)