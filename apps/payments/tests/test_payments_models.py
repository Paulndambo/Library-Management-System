from django.core.paginator import Paginator
from django.test import Client, TestCase
from django.urls import reverse

from apps.library.models import Book
from apps.payments.models import Transaction
from apps.users.models import Member, User


class PaymentsModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="James",
            last_name="Doe",
            phone_number="0745491093",
            id_number="123456789",
            email="jamesdoe@gmail.com",
            username="jamesdoe",
            gender="Male",
            address="228-90119",
            city="Machakos",
            country="Kenya",
        )
        self.user.set_password("1234")
        self.user.save()

        self.member = Member.objects.create(
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

        self.book = Book.objects.create(
            title="The richest man in the babylon",
            author="Babylon Author",
            year_published="1929",
            genre="Finance",
            price=305.0,
            rental_fee=15.0,
            quantity=30,
            rented_out=4,
            available=True
        )


        self.client = Client()

        self.client.login(username='jamesdoe', password='1234')


    def test_transaction_can_be_created(self):
        payment = Transaction.objects.create(
            paid_by=self.member, 
            book=self.book,
            amount_paid=305.0,
            payment_type="Book Issue",
            received_by=self.user
        )

        self.assertEqual(str(payment), f"{payment.paid_by.name} has paid {payment.amount_paid} for {payment.payment_type}")
        self.assertIsInstance(payment.amount_paid, float)