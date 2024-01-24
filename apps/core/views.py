from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.library.models import Book, BookIssue
from apps.users.models import Member

date_today = datetime.now().date()

# Create your views here.
@login_required(login_url="/users/login/")
def home(request):
    books_count = Book.objects.count()
    members_count = Member.objects.count()

    """
    => Checking for issued books which should have been returned up to today
    """
    book_issues_overdue = BookIssue.objects.filter(status="Active").filter(borrowed_to__lt=date_today)
    
    if book_issues_overdue:
        book_issues_overdue.update(status="Overdue")

    """
    => Updating the return fee based on the number of days exceeded on the agreed
        book return date
    """
    overdue_book_issues = BookIssue.objects.filter(status="Overdue")
    if overdue_book_issues:
        for overdue_book_issue in overdue_book_issues:
            days_passed = (date_today - overdue_book_issue.borrowed_to).days

            return_fee = (overdue_book_issue.return_fee * 0.15) * days_passed
            overdue_book_issue.return_fee = return_fee
            overdue_book_issue.save()

    context = {
        "books_count": books_count,
        "members_count": members_count
    }
    return render(request, "home.html", context)