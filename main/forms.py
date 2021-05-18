from django.core import validators
from django import forms
from .models import Contact
from phonenumber_field.modelfields import PhoneNumberField


class UserQuery(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'Mobile_no', 'Elaborate_Your_Concern']
        error_messages = {
            'name': {'required': 'Enter Your Name '},
            'email': {'required': 'Enter Your email '},
            'Mobile_no': {'required': 'Enter Your Mobile no.'},
            'Elaborate_Your_Concern': {'required': 'Enter Your Elaborate Your Concern'}
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'Mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
            'Elaborate_Your_Concern': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
        }
