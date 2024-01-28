from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.core.constants import GENDER_CHOICES, ROLE_CHOICES
from apps.core.models import AbstractBaseModel


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(choices=ROLE_CHOICES, max_length=255, default="Librarian")
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.username

    def name(self):
        return f"{self.first_name} {self.last_name}"


class Member(AbstractBaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    outstanding_debt = models.DecimalField(max_digits=20, decimal_places=2, default=0)


    def __str__(self):
        return self.name


