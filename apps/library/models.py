from django.db import models

from apps.core.constants import BOOK_GENRES, BOOK_ISSUE_STATUS
from apps.core.models import AbstractBaseModel


# Create your models here.
class Book(AbstractBaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_published = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=BOOK_GENRES)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    rental_fee = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    rented_out = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def available_books(self):
        return self.quantity - self.rented_out


class BookIssue(AbstractBaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey("users.Member", on_delete=models.SET_NULL, null=True, related_name="memberissuedbooks")
    borrowed_from = models.DateField()
    borrowed_to = models.DateField()
    status = models.CharField(max_length=255, choices=BOOK_ISSUE_STATUS)
    return_fee = models.DecimalField(max_digits=100, decimal_places=2)
    overdue_fee = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.member.name} has been issued with {self.book.title}"

    @property
    def total_fee_expected(self):
        return self.return_fee + self.overdue_fee