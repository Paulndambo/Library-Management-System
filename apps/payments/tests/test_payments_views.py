from django.core.paginator import Paginator
from django.test import Client, TestCase
from django.urls import reverse

from apps.library.models import Book
from apps.payments.models import Transaction
from apps.users.models import Member, User


class PaymentsViewTestCase(TestCase):
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

    def test_payments_view_with_transactions(self):
        Transaction.objects.create(
            paid_by=self.member, 
            book=self.book,
            amount_paid=305.0,
            payment_type="Book Issue",
            received_by=self.user
        )
        Transaction.objects.create(
            paid_by=self.member, 
            book=self.book,
            amount_paid=305.0,
            payment_type="Book Issue",
            received_by=self.user
        )
        Transaction.objects.create(
            paid_by=self.member, 
            book=self.book,
            amount_paid=305.0,
            payment_type="Book Issue",
            received_by=self.user
        )
        
        response = self.client.get(reverse('payments'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payments.html')

        self.assertIn('page_obj', response.context)
        page_obj = response.context['page_obj']
        self.assertEqual(page_obj.object_list.count(0), 0)


    def test_payments_view_without_transactions(self):
        response = self.client.get(reverse('payments'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'payments/payments.html')

        self.assertIn('page_obj', response.context)
        page_obj = response.context['page_obj']
        self.assertEqual(page_obj.object_list.count(), 0)


    def test_payments_view_requires_login(self):
        self.client.logout()

        response = self.client.get(reverse('payments'))

        self.assertRedirects(response, '/users/login/?next=' + reverse('payments'))
