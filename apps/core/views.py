from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.library.models import Book
from apps.users.models import Member


# Create your views here.
def home(request):
    books_count = Book.objects.count()
    members_count = Member.objects.count()

    context = {
        "books_count": books_count,
        "members_count": members_count
    }
    return render(request, "home.html", context)