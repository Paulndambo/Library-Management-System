from datetime import datetime
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.library.models import Book, BookIssue
from apps.payments.models import Transaction
from apps.users.models import Member


# Create your views here.
@login_required(login_url="/users/login/")
def books(request):
    books = Book.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")
        books = Book.objects.filter(
            Q(title__icontains=search_text) | 
            Q(author__icontains=search_text)
        ).order_by("-created")


    paginator = Paginator(books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "books/books.html", context)


@login_required(login_url="/users/login/")
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


@login_required(login_url="/users/login/")
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
        book.title = title
        book.author = author
        book.year_published = year_published
        book.genre = genre if genre else book.genre
        book.price = price
        book.rental_fee = rental_fee
        book.quantity = quantity
        book.save()

        return redirect("books")
    return render(request, "books/edit_book.html")


@login_required(login_url="/users/login/")
def delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect("books")

    return render(request, "books/delete_book.html")


@login_required(login_url="/users/login/")
def issued_books(request):
    issued_books = BookIssue.objects.all().order_by("-created")

    if request.method == "POST":
        search_text = request.POST.get("search_text")

        issued_books = BookIssue.objects.filter(
            Q(book__title__icontains=search_text) | 
            Q(book__author__icontains=search_text) | 
            Q(member__name__icontains=search_text) |
            Q(member__id_number__icontains=search_text)
        ).order_by("-created")

    paginator = Paginator(issued_books, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    """
    => Making sure that;-
        1. Only members with outstanding debt below 500 can be given books.
        2. Only books not fully rented out are available to be issued
    """
    members = Member.objects.filter(outstanding_debt__lte=500.0)
    books = Book.objects.filter(available=True)

    context = {
        "page_obj": page_obj,
        "members": members,
        "books": books
    }
    return render(request, "issued_books/issued_books.html", context)


@login_required(login_url="/users/login/")
@transaction.atomic
def new_book_issue(request):
    user = request.user
    if request.method == "POST":
        try:
            book_id = request.POST.get("book_id")
            member_id = request.POST.get("member_id")
            borrowed_from = request.POST.get("borrowed_from")
            borrowed_to = request.POST.get("borrowed_to")

            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)

            BookIssue.objects.create(
                book=book,
                member=member,
                borrowed_from=borrowed_from,
                borrowed_to=borrowed_to,
                status="Active",
                return_fee=book.rental_fee,
                overdue_fee=0
            )

            book.rented_out += 1
            book.save()

            Transaction.objects.create(
                paid_by=member,
                book=book,
                received_by=user,
                amount_paid=book.rental_fee,
                payment_type="Book Issue"
            )

            if book.rented_out == book.quantity:
                book.available=False
                book.save()

            return redirect("issued-books")
        except Exception as e:
            raise e

    return render(request, "issued_books/new_book_issue.html")


@login_required(login_url="/users/login/")
@transaction.atomic
def return_book(request):
    user = request.user
    if request.method == "POST":
        issued_book_id = request.POST.get("issued_book_id")
        return_fee = Decimal(request.POST.get("return_fee"))

        issued_book = BookIssue.objects.get(id=issued_book_id)

        issued_book.book.rented_out -= 1
        issued_book.book.save()

        issued_book.status = "Returned"
        issued_book.save()

        
        Transaction.objects.create(
            book=issued_book.book,
            paid_by=issued_book.member,
            amount_paid=return_fee,
            payment_type="Return Fee",
            received_by=user
        )
        return redirect("issued-books")
    return render(request, "issued_books/return_book.html")


@login_required(login_url="/users/login/")
def refresh_book_issue(request, book_issue_id):
    book_issue = BookIssue.objects.get(id=book_issue_id)


@login_required(login_url="/users/login/")
def delete_book_issue(request):
    if request.method == "POST":
        issued_book_id = request.POST.get("issued_book_id")
        issued_book = BookIssue.objects.get(id=issued_book_id)
        issued_book.delete()

        return redirect("issued-books")

    return render(request, "issued_books/delete_book_issue.html")
