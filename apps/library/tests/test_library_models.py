from django.test import TestCase

from apps.library.models import Book, BookIssue
from apps.users.models import Member

class TestLibraryModelsTestCase(TestCase):
    def setUp(self) -> None:
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
        return super().setUp()

    def test_book_can_be_created(self):
        book = Book.objects.create(
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

        self.assertEqual(str(book), "The richest man in the babylon")

        return book

    def test_book_can_be_issued(self):
        book = self.test_book_can_be_created()

        book_issue = BookIssue.objects.create(
            book=book,
            member=self.member,
            borrowed_from="2024-01-23",
            borrowed_to="2024-02-14",
            status="Active",
            return_fee=book.rental_fee,
            overdue_fee=0.0
        )

        self.assertEqual(book_issue.return_fee, 15.0)