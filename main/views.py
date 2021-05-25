# from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import UserQuery
from .models import Contact
from django.contrib import messages

# Create your views here.


# without login
def index(request):
    return render(request, "main/index.html")


# without login
def about(request):
    return render(request, "main/index.html")


# without login
def help(request):
    return render(request, "main/index.html")


# without login
def contact(request):
    if request.method == 'POST':
        fm = UserQuery(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mn = fm.cleaned_data['Mobile_no']
            concern = fm.cleaned_data['Elaborate_Your_Concern']
            reg = Contact(name=nm, email=em, Mobile_no=mn,
                          Elaborate_Your_Concern=concern)
            reg.save()
            messages.success(
                request, 'Your message has been successfully submitted')
            fm = UserQuery()

    else:
        fm = UserQuery()
    return render(request, 'main/contact.html', {'form': fm})


# for redirect to dashboard as type
def dashboardAsType(request):
    if request.user.is_authenticated:
        if request.user.profile.type() == "student":
            return redirect('student/')

        elif request.user.profile.type() == "director":
            return redirect('test')

        elif request.user.profile.type() == "hod":
            return redirect('test')

        elif request.user.profile.type() == "teacher":
            return redirect('test')

    return redirect('home')


# for login
def loginHandle(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        loginUsername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginUsername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            return redirect('studentHome')

        else:
            messages.error(
                request, "Invalid credential!, please try again")
    return render(request, "main/login.html")


def logOutHandle(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('home')
    else:
        return redirect("home")


# for html template testing
def test(request):
    return render(request, "main/error.html")
