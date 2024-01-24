from django.urls import path

from apps.payments.views import payments

urlpatterns = [
    path("", payments, name="payments"),
]