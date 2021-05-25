from django.shortcuts import redirect, render
from student.models import Student
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'staff/index.html')


def addStudent(request):
    # if request.method == 'POST':

    username = "parkash"  # request.POST['username']
    first_name = "parkash"  # request.POST['first_name']
    last_name = "verma"  # request.POST['last_name']
    email = "prakash2@verma.com"  # request.POST['email']
    password = "prakash2@verma.com"  # request.POST['password']
    branch = "cse"  # request.POST['branch']

    stu = Student.create_student(username=username, password=password,
                                 email=email, branch=branch, first_name=first_name, last_name=last_name)

    messages.success(
        request, f'New Student "{username}" has been successfully Added!!')
    return redirect("home")


def addTeacher(request):
    # if request.method == 'POST':

    username = "onkar"  # request.POST['username']
    first_name = "onkar"  # request.POST['first_name']
    last_name = "thakur"  # request.POST['last_name']
    email = "onkar@verma.com"  # request.POST['email']
    password = "onkar@verma.com"  # request.POST['password']
    department = "cse"  # request.POST['branch']

    stu = Student.create_student(username=username, password=password,
                                 email=email, department=department, first_name=first_name, last_name=last_name)

    messages.success(
        request, f'New teacher "{username}" has been successfully Added!!')
    return redirect("home")

def addHod(request):
    # if request.method == 'POST':

    username = "onkar6"  # request.POST['username']
    first_name = "onkar6"  # request.POST['first_name']
    last_name = "thakur"  # request.POST['last_name']
    email = "onkar6@verma.com"  # request.POST['email']
    password = "onkar6@verma.com"  # request.POST['password']
    department = "cse"  # request.POST['branch']

    stu = Student.create_teacher(username=username, password=password,
                                 email=email, department=department, first_name=first_name, last_name=last_name)

    messages.success(
        request, f'New teacher "{username}" has been successfully Added!!')
    return redirect("home")
