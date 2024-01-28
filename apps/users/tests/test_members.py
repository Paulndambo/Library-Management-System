from django.test import Client, TestCase
from django.urls import reverse

from apps.users.models import Member, User


class MemberTestCase(TestCase):
    def setUp(self) -> None:
        self.member = Member.objects.create(
            name="Jane Doe",
            email="janedoe@gmail.com",
            phone_number="0745491093",
            id_number="123E456789",
            gender="Male",
            address="228-90119",
            city="Machakos",
            county="Machakos",
            country="Kenya",
            outstanding_debt=200.0
        )

        self.user = User.objects.create(
            first_name="Jane",
            last_name="Doe",
            username="janedoeii",
            email="janedoeii@gmail.com",
            phone_number="0745491093",
            id_number="123E456789",
            gender="Male",
            address="228-90119",
            city="Machakos",
            country="Kenya",
        )
        self.user.set_password("1234")

        self.client.login(username="janedoeii", password="1234")

        return super().setUp()


    def test_member_name_is_str(self):
        self.assertIsInstance(self.member.name, str)

    def test_member_debt_is_float(self):
        self.assertIsInstance(self.member.outstanding_debt, float)

    def test_member_can_be_created(self):
        member = Member.objects.create(
            name="John Doe",
            email="johndoe@gmail.com",
            phone_number="0745491093",
            id_number="123456789",
            gender="Male",
            address="228-90119",
            city="Machakos",
            county="Machakos",
            country="Kenya",
            outstanding_debt=100.0
        )

        self.assertEqual(str(member), "John Doe")

    def test_member_editing(self):
        data = {
            "member_id": self.member.id,
            "name": "Jane Doe II",
            "email": "janedoe@gmail.com",
            "phone_number": "+254745491093",
            "id_number": "56789GHJKJAHA",
            "gender": "Female",
            "address": "59-90119",
            "city": "Matuu",
            "county": "Machakos",
            "country": "Kenya",
            "outstanding": 250.0
        }
        response = self.client.post(reverse('edit-member'), data)
        self.assertEqual(response.status_code, 302)
