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
    Elaborate_Your_Concern = models.CharField(max_length=1000)
    Mobile_no = PhoneNumberField(blank=True)
    execution_time = models.TimeField(
        auto_now=False, auto_now_add=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)

    def type(self) -> str:
        if  self.is_student:
            return "student"
            
        elif self.is_teacher:
            return "teacher"

        elif self.is_hod:
            return "hod"

        elif self.is_director:
            return "director"
        
        else:
            return "visitor"

    def __str__(self):
        return self.user.username
        
        

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
