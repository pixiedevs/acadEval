from django.contrib.auth.models import Group, User
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=10, blank=True)
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
    time = models.TimeField(auto_now_add=True, blank=True)


class Teacher(Staff):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create_teacher(cls, username, password, email=None, department=None, first_name=None, last_name=None):
        stu = Teacher()
        new_user = User.objects.create_user(username, email, password)

        my_group, created = Group.objects.get_or_create(name='teacher')
        my_group.user_set.add(new_user)

        if first_name is not None:
            new_user.first_name = first_name
        if last_name is not None:
            new_user.last_name = last_name

        new_user.profile.is_teacher = True
        new_user.save()

        stu.user = new_user
        if department is not None:
            stu.department = department
        stu.save()

        return stu

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Hod(Staff):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create_hod(cls, username, password, email=None, department=None, first_name=None, last_name=None):
        stu = Hod()
        new_user = User.objects.create_user(username, email, password)

        my_group, created = Group.objects.get_or_create(name='hod')
        my_group.user_set.add(new_user)

        if first_name is not None:
            new_user.first_name = first_name
        if last_name is not None:
            new_user.last_name = last_name

        new_user.profile.is_hod = True
        new_user.save()

        stu.user = new_user
        if department is not None:
            stu.department = department
        stu.save()

        return stu

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class Director(Staff):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create_director(cls, username, password, email=None, department=None, first_name=None, last_name=None):
        stu = Director()
        new_user = User.objects.create_user(username, email, password)

        my_group, created = Group.objects.get_or_create(name='director')
        my_group.user_set.add(new_user)

        if first_name is not None:
            new_user.first_name = first_name
        if last_name is not None:
            new_user.last_name = last_name

        new_user.profile.is_director = True
        new_user.save()

        stu.user = new_user
        if department is not None:
            stu.department = department
        stu.save()

        return stu

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
