from django.contrib.auth.models import User, Group
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.


class Student(models.Model):
    # for debugging, in production change it to on_delete=models.PROTECT
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, to_field='username', db_column='username', primary_key=True, related_name='student')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100, unique=True)
    father_name = models.CharField(max_length=70, blank=True)
    student_id = models.CharField(max_length=70, unique=True)
    # enrollment = models.CharField(max_length=70, blank=True, unique=True)
    batch_year = models.IntegerField(blank=True, null=True)
    branch = models.CharField(max_length=10, blank=True)
    current_address = models.CharField(max_length=1000, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    father_mobile_no = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=10, blank=True)
    guardian_mobile_no = PhoneNumberField(blank=True)
    guardian_name = models.CharField(max_length=50, blank=True)
    mobile_no = PhoneNumberField(blank=True)
    permanent_address = models.CharField(max_length=1000, blank=True)
    semester = models.IntegerField(default=1, blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    year = models.IntegerField(default=1, blank=True)

    def __str__(self) -> str:
        return self.user.username

    @property
    def full_name(self) -> str:
        return self.first_name + " " + self.last_name

    @classmethod
    def create_student(cls, username, password, email=None, branch=None, first_name=None, last_name=None, student_id=None, date_of_birth=None, semester=None, year=None, batch_year=None):
        stu = Student()
        new_user, created = User.objects.get_or_create(
            username, email, password)

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

        if student_id is not None:
            stu.student_id = student_id
        if date_of_birth is not None:
            stu.date_of_birth = date_of_birth
        if semester is not None:
            stu.semester = semester
        if year is not None:
            stu.year = year
        if batch_year is not None:
            stu.batch_year = batch_year

        stu.save()

        return stu

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def get_attendance_by_sem_month(self, sem=None, month=None):
        if sem is None:
            sem = self.semester
        if month is None:
            month = self.time.date().month

        attendance = self.attendance.filter(
            semester=sem, date__icontains=f'{month}-').all()

        return attendance


class StudentAttendance(models.Model):
    # foreignKey is for manyToOne relationship
    student = models.ForeignKey(
        Student, related_name='attendance', on_delete=models.CASCADE, to_field="student_id")
    semester = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} {self.date} {self.is_present}"

    @property
    def enrollment(self):
        return self.student.user.username

    # for preventing duplicate attendance
    class Meta:
        unique_together = ("student_id", "date",)


# Student's Books
class Book(models.Model):
    student = models.ForeignKey(
        Student, related_name='book', on_delete=models.CASCADE, to_field="student_id")
    book_id = models.CharField(max_length=50)
    book_name = models.CharField(max_length=100)
    issue_date = models.DateField(default=datetime.date.today)
    expiry_date = models.DateField()

    # for preventing
    # class Meta:
        # unique_together = ("student", "book_id")


# Student's Marks
class Mark(models.Model):
    student = models.ForeignKey(
        Student, related_name='mark', on_delete=models.CASCADE, to_field="student_id")
    semester = models.PositiveIntegerField()
    result = models.CharField(max_length=4)
    sgpa = models.FloatField(verbose_name="SGPA")
    cgpa = models.FloatField(verbose_name="CGPA")
    file = models.FileField(upload_to='student_media/marks', unique=True)

    def file_url(self) -> str:
        return f'{self.file.url}'


class StudentClass(models.Model):
    subject = models.CharField(max_length=50)
    tutor = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username")
    semester = models.PositiveIntegerField(default=1)
    branch = models.CharField(default="CSE", max_length=10)

    url = models.URLField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name_plural = "Student Classes"
