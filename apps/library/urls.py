from django.urls import path

from apps.library.apis.views import BookRateAPIView
from apps.library.views import (books, delete_book, delete_transaction,
                                edit_book, new_book, new_transaction,
                                return_book, transactions)

urlpatterns = [
    path("books/", books, name="books"),
    path("new-book/", new_book, name="new-book"),
    path("edit-book/", edit_book, name="edit-book"),
    path("delete-book/", delete_book, name="delete-book"),
    path("book-rate/", BookRateAPIView.as_view(), name="book-rate"),

    # Transactions URLS
    path("transactions/", transactions, name="transactions"),
    path("new-transaction/", new_transaction, name="new-transaction"),
    path("delete-transaction/", delete_transaction, name="delete-transaction"),
    path("return-book/", return_book, name="return-book"),
]
