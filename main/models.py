from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# from datetime import datetime, date

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=1000)
    mobile_no = PhoneNumberField(blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    data = models.JSONField(default=dict)

    @property
    def type(self) -> str:
        return "student" if self.is_student else "teacher" if self.is_teacher else "hod" if self.is_hod else "director" if self.is_director else "visitor"

    @property
    def staff(self):
        return self.user.student if self.is_student else self.user.teacher if self.is_teacher else self.user.hod if self.is_hod else self.user.director if self.is_director else None

    @property
    def is_staff(self):
        return True if (self.is_teacher or self.is_hod or self.is_director) else False

    @property
    def type_url(self):
        return "staff" if (self.is_teacher or self.is_hod or self.is_director) else "student" if self.is_student else ""

    def has_permission(self, creator):
        if creator is None:
            return False
            
        elif self.user == creator or (creator.profile.is_director and self.staff().college == creator.profile.staff.college):
            return True
            
        else:
            return False

        # print(self.staff(), creator)


class Notice(models.Model):
    title = models.CharField(max_length=60)
    branch = models.CharField(max_length=10, default='CSE')
    created_by = models.ForeignKey(
        User, related_name='notice', on_delete=models.CASCADE, to_field="username")

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.created_at} - {self.modified_at} - {self.title}"


class College(models.Model):
    # for short college name like TITM, TITS, TITE and TITA etc
    college = models.CharField(max_length=10, default="TITS", primary_key=True)
    college_full_name = models.CharField(max_length=100, unique=True)
    college_code = models.IntegerField(unique=True)
    college_bio = models.CharField(max_length=1000)


# signal's for create Profile's object/row while new creating user's object/row 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
