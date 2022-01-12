from main.decoraters import auth_req, unauth_req
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
    return render(request, "main/about.html")


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
            mn = fm.cleaned_data['mobile_no']
            concern = fm.cleaned_data['message']
            reg = Contact(name=nm, email=em, mobile_no=mn,
                          message=concern)
            reg.save()
            messages.success(
                request, 'Your message has been successfully submitted')
            fm = UserQuery()

    else:
        fm = UserQuery()
    return render(request, 'main/contact.html', {'form': fm})


# for redirect to dashboard as type
@auth_req
def dashboardAsType(request):
    if request.user.profile.type == "student":
        return redirect('studentHome')

    elif request.user.profile.type == "director":
        return redirect('s_Home')

    elif request.user.profile.type == "hod":
        return redirect('s_Home')

    elif request.user.profile.type == "teacher":
        return redirect('s_Home')

    return redirect('home')


# for login
@unauth_req
def loginHandle(request):
    if request.method == 'POST':
        loginUsername = request.POST['username']
        loginpassword = request.POST['password']
        print(loginpassword)

        user = authenticate(username=loginUsername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            return redirect('home')

        else:
            messages.error(
                request, "Invalid credential!, please try again")
    return render(request, "main/login.html")


@auth_req
def logOutHandle(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')


# for html template testing
def test(request):
    return render(request, "main/error.html")
