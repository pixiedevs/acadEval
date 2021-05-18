from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegister
from .models import Student
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'student/index.html')


def student(request):
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            fm = fm.cleaned_data['father_name']
            em = fm.cleaned_data['email']
            mn = fm.cleaned_data['Mobile_no']
            fmn = fm.cleaned_data['father_mobile_no']
            ca = fm.cleaned_data['Current_Address']
            pa = fm.cleaned_data['Parmanent_Address']
            br = fm.cleaned_data['Branch']
            by = fm.cleaned_data['Batch_year']
            reg = Student(first_name=fn, last_name=ln, father_name=fm, email=em, Mobile_no=mn,
                          father_mobile_no=fmn, Current_Address=ca, Parmanent_Address=pa, Branch=br, Batch_year=by)
            reg.save()
            messages.success(
                request, 'New Student has been successfully Added!!')
            fm = StudentRegister()

    else:
        fm = StudentRegister()
    return render(request, 'student/stu.html', {'form': fm})
