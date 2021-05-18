from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from datetime import datetime,date

# Create your models here.
# Student by vishal


class Student(models.Model):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    father_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    Mobile_no = PhoneNumberField(blank=True)
    father_mobile_no = PhoneNumberField(blank=True)
    Current_Address = models.CharField(max_length=1000)
    Parmanent_Address = models.CharField(max_length=1000)
    Branch = models.CharField(max_length=10)
    Batch_year = models.IntegerField()
    time = models.TimeField(auto_now_add=True, blank=True)
