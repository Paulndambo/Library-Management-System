from datetime import datetime
from decimal import Decimal

from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from apps.library.models import Book, BookIssue
from apps.users.models import Member


# Create your views here.
def books(request):
    books = Book.objects.all()

    paginator = Paginator(books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "books/books.html", context)


def new_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year_published = request.POST.get("year_published")
        genre = request.POST.get("genre")
        price = request.POST.get("price")
        rental_fee = request.POST.get("rental_fee")
        quantity = request.POST.get("quantity")

        print(f"Title: {title}, Genre: {genre}, Author: {author}")

        book = Book.objects.create(
            title=title,
            author=author,
            year_published=year_published,
            genre=genre,
            price=price,
            rental_fee=rental_fee,
            quantity=quantity
        )

        return redirect("books")
    return render(request, "books/new_book.html")



def edit_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        title = request.POST.get("title")
        author = request.POST.get("author")
        year_published = request.POST.get("year_published")
        genre = request.POST.get("genre")
        price = request.POST.get("price")
        rental_fee = request.POST.get("rental_fee")
        quantity = request.POST.get("quantity")

        book = Book.objects.get(id=book_id)
        book.title=title
        book.author=author
        book.year_published=year_published
        book.genre=genre if genre else book.genre
        book.price=price
        book.rental_fee=rental_fee
        book.quantity=quantity
        book.save()

        return redirect("books")
    return render(request, "books/edit_book.html")


def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect("books")

    return render(request, "books/delete_book.html")



def issued_books(request):
    issued_books = BookIssue.objects.all()

    paginator = Paginator(issued_books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    members = Member.objects.all()
    books = Book.objects.all()

    context = {
        "page_obj": page_obj,
        "members": members,
        "books": books
    }
    return render(request, "issued_books/issued_books.html", context)


def new_book_issue(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        member_id = request.POST.get("member_id")
        borrowed_from = request.POST.get("borrowed_from")
        borrowed_to = request.POST.get("borrowed_to")


        member = Member.objects.get(id=member_id)
        book = Book.objects.get(id=book_id)

        book_issue = BookIssue.objects.create(
            book=book,
            member=member,
            borrowed_from=borrowed_from,
            borrowed_to=borrowed_to,
            status="Active",
            return_fee=book.rental_fee,
            overdue_fee=0
        )

        return redirect("issued-books")

    return render(request, "issued_books/new_book_issue.html")


def return_book(request):
    if request.method == "POST":
        issued_id = request.POST.get("issued_book_id")
        return_fee = Decimal(request.POST.get("return_fee"))

        pass

    return render(request, "issued_books/return_book.html")


def refresh_book_issue(request, book_issue_id):
    book_issue = BookIssue.objects.get(id=book_issue_id)




def delete_book_issue(request):
    if request.method == "POST":
        issued_book_id = request.POST.get("issued_book_id")
        issued_book = BookIssue.objects.get(id=issued_book_id)
        issued_book.delete()

        return redirect("issued-books")

    return render(request, "issued_books/delete_book_issue.html")