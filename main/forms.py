from django.core import validators
from django import forms
from .models import Contact
from phonenumber_field.modelfields import PhoneNumberField


class UserQuery(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile_no', 'message']
        error_messages = {
            'name': {'required': 'Enter Your Name '},
            'email': {'required': 'Enter Your email '},
            'mobile_no': {'required': 'Enter Your Mobile no.'},
            'message': {'required': 'Enter Your Elaborate Your Concern'}
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
        }
