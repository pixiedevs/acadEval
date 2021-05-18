from django.core import validators
from django import forms
from .models import Student
from phonenumber_field.modelfields import PhoneNumberField

# Student by vishal


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'father_name', 'email', 'Mobile_no',
                  'father_mobile_no', 'Current_Address', 'Parmanent_Address', 'Branch', 'Batch_year']
        error_messages = {
            'name': {'required': 'Enter Your Name '},
            'email': {'required': 'Enter Your email '},
            'Mobile_no': {'required': 'Enter Your Mobile no.'},
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'Mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
        }
