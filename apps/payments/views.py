from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from apps.payments.models import Transaction


# Create your views here.
@login_required(login_url="/users/login/")
def payments(request):
    transactions = Transaction.objects.all().order_by("-created")


    paginator = Paginator(transactions, 13)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "payments/payments.html", context)
