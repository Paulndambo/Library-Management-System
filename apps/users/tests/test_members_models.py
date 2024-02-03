from django.test import TestCase

from apps.users.models import Member


class MemberModelsTestCase(TestCase):

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

        return member

    def test_member_can_be_stringfied(self):
        member = self.test_member_can_be_created()

        self.assertEqual(str(member), "John Doe")

    
    def test_member_data_types(self):
        member = self.test_member_can_be_created()

        self.assertIsInstance(member.name, str)
        self.assertIsInstance(member.outstanding_debt, float)
        self.assertIsInstance(member.id, int)