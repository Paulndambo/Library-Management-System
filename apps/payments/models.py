from django.db import models

from apps.core.constants import PAYMENT_TYPES
from apps.core.models import AbstractBaseModel


# Create your models here.
class Transaction(AbstractBaseModel):
    paid_by = models.ForeignKey("users.Member", on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey("library.Book", on_delete=models.SET_NULL, null=True)
    amount_paid = models.DecimalField(max_digits=100, decimal_places=2)
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPES)
    received_by = models.ForeignKey("users.User", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.paid_by.name} has paid {self.amount_paid} for {self.payment_type}"