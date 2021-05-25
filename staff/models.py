from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=10, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    mobile_no = PhoneNumberField(blank=True)
    current_address = models.CharField(max_length=100, blank=True)
    permanent_address = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    present_position = models.CharField(max_length=50, blank=True)
    qualification = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=10, blank=True)
    college_full_name = models.CharField(max_length=100, blank=True)
    expertise = models.CharField(max_length=100, blank=True)
    joining_time = models.DateField(null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)


class Teacher(Staff):
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_user.username


class Hod(Staff):
    hod_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hod_user.username
