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



def transactions(request):
    transactions = BookIssue.objects.all()

    paginator = Paginator(transactions, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "transactions/transactions.html", context)


def new_transaction(request):
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

        return redirect("transactions")

    return render(request, "transactions/new_transaction.html")



def delete_transaction(request):
    if request.method == "POST":
        transaction_id = request.POST.get("transaction_id")
        transaction = BookIssue.objects.get(id=transaction_id)
        transaction.delete()

        return redirect("transactions")

    return render(request, "transactions/delete_transaction.html")