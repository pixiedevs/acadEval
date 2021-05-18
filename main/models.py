from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, date

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    Elaborate_Your_Concern = models.CharField(max_length=1000)
    Mobile_no = PhoneNumberField(blank=True)
    execution_time = models.TimeField(
        auto_now=False, auto_now_add=True, blank=True)
