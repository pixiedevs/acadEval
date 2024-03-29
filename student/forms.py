from django.core import validators
from django import forms
from .models import Student, Book
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# Student by vishal


class AddStudentForm(forms.ModelForm):
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            'username': {'required': 'Enter your username '},
            'password': {'required': 'Enter your  password '},
        }


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'father_name', 'student_id', 'email', 'mobile_no',
                  'father_mobile_no', 'current_address', 'permanent_address', 'branch', 'batch_year']
        error_messages = {
            'first_name': {'required': 'Enter your first name '},
            'last_name': {'required': 'Enter your last name '},
            'father_name': {'required': 'Enter your father name '},
            'student_id':  {'required': 'Enter your Id name '},
            'email': {'required': 'Enter your email '},
            'mobile_no': {'required': 'Enter your Mobile no.'},
            'father_mobile_no': {'required': 'Enter your father mobile no.  '},
            'current_address': {'required': 'Enter your  current address '},
            'permanent_address': {'required': 'Enter your  permanent address '},
            'branch': {'required': 'Enter your  branch '},
            'batch_year': {'required': 'Enter your  batch year '},
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Last Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Father Name'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Id'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Mobile No'}),
            'father_mobile_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Father Mobile No'}),
            'current_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Current Address'}),
            'permanent_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your Permanent Address'}),
            'branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Branch'}),
            'batch_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Batch Year'}),
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'book_name', 'issue_date', 'expiry_date']
        labels = {'book_id': 'Book Id', 'book_name': 'Book Name',
                  'issue_date': 'Issue Date', 'expiry_date': 'Expiry Date'}
        widgets = {
            'book_id': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.Textarea(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
