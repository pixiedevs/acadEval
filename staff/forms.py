from django.core import validators
from django import forms
from .models import Teacher, Hod
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# Teacher by vishal
# this is form for teacher


class AddTeacherForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {'required': 'Enter your username '},
            'password': {'required': 'Enter your  password '},
        }


class TeacherDataForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'mobile_no',
                  'current_address', 'permanent_address', 'department']
        labels = {'email': 'Email', 'permanent_address': 'Permanent Address',
                  'department': 'Department'}
        error_messages = {
            'first_name': {'required': 'Enter your first name '},
            'last_name': {'required': 'Enter your last name '},
            'email': {'required': 'Enter your email '},
            'mobile_no': {'required': 'Enter your Mobile no.'},
            'gender': {'required': 'Enter your gender'},
            'current_address': {'required': 'Enter your  current address '},
            'permanent_address': {'required': 'Enter your  permanent address '},
            'department': {'required': 'Enter your  department '},
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'gender': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Department'}),
        }

# this is form for HOD


class AddHodForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {'required': 'Enter your username '},
            'password': {'required': 'Enter your  password '},
        }


class HodDataForm(forms.ModelForm):
    class Meta:
        model = Hod
        fields = ['first_name', 'last_name', 'email', 'mobile_no',
                  'current_address', 'permanent_address', 'department']
        error_messages = {
            'first_name': {'required': 'Enter your first name '},
            'last_name': {'required': 'Enter your last name '},
            'email': {'required': 'Enter your email '},
            'mobile_no': {'required': 'Enter your Mobile no.'},
            'gender': {'required': 'Enter your gender'},
            'current_address': {'required': 'Enter your  current address '},
            'permanent_address': {'required': 'Enter your  permanent address '},
            'department': {'required': 'Enter your  department '},
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
            'gender': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Query'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Department'}),
        }
