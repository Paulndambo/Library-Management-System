from django.urls import path

from apps.library.apis.views import BookRateAPIView
from apps.library.views import (books, delete_book, delete_book_issue,
                                edit_book, issued_books, new_book,
                                new_book_issue, return_book)

urlpatterns = [
    path("books/", books, name="books"),
    path("new-book/", new_book, name="new-book"),
    path("edit-book/", edit_book, name="edit-book"),
    path("delete-book/", delete_book, name="delete-book"),
    path("book-rate/", BookRateAPIView.as_view(), name="book-rate"),

    # Transactions URLS
    path("issued-books/", issued_books, name="issued-books"),
    path("new-book-issue/", new_book_issue, name="new-book-issue"),
    path("delete-book-issue/", delete_book_issue, name="delete-book-issue"),
    path("return-book/", return_book, name="return-book"),
]
