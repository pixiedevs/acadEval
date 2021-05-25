from django.contrib.auth.models import User, Group
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Student(models.Model):
    # for debugging, in production change it to on_delete=models.PROTECT
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
    semester = models.IntegerField(default=1, blank=True)
    year = models.IntegerField(default=1, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    guardian_name = models.CharField(max_length=50, blank=True)
    guardian_mobile_no = PhoneNumberField(blank=True)
    time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user.username
        
    @classmethod
    def create_student(cls, username, password, email=None, branch=None, first_name=None, last_name=None):
        stu = Student()
        new_user = User.objects.create_user(username, email, password)

        my_group, created = Group.objects.get_or_create(name='student')
        my_group.user_set.add(new_user)

        if first_name is not None:
            new_user.first_name = first_name
        if last_name is not None:
            new_user.last_name = last_name

        new_user.profile.is_student = True
        new_user.save()

        stu.user = new_user
        if branch is not None:
            if not branch.isupper():
                branch = branch.upper()
            stu.branch = branch
        stu.save()

        return stu

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


# class StudentAttendance(models.Model):
#     # foreignKey is for manyToOne relationship
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     semester = models.PositiveIntegerField()
#     date = models.DateField(auto_now_add=True)
#     is_present = models.BooleanField(default=False)

# class College(models.Model):
#     # for short college name like TITM, TITS, TITE and TITA etc
#     college = models.CharField(max_length=10)
#     college_full_name = models.CharField(max_length=100)
#     college_code = models.IntegerField()
#     college_bio = models.CharField(max_length=1000)
