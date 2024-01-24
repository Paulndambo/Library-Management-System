from django.contrib import admin

from apps.library.models import Book, BookIssue


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "quantity", "rental_fee", "available", "available_books"]

@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ["id", "member", "book", "borrowed_from", "borrowed_to", "status", "return_fee", "overdue_fee"]