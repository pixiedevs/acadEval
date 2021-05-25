from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    father_name = models.CharField(max_length=70, blank=True)
    student_id = models.CharField(max_length=70, blank=True)
    mobile_no = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    father_mobile_no = PhoneNumberField(blank=True)
    current_address = models.CharField(max_length=1000, blank=True)
    permanent_address = models.CharField(max_length=1000, blank=True)
    branch = models.CharField(max_length=10, blank=True)
    batch_year = models.IntegerField(default=int(datetime.now().year)+4)
    semester = models.IntegerField(blank=True)
    year = models.IntegerField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    guardian_name = models.CharField(max_length=50, blank=True)
    guardian_mobile_no = PhoneNumberField(blank=True)
    time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username
