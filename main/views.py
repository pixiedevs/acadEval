from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
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

# for login


def login(request):
    return render(request, "main/index.html")


# for html template testing
def test(request):
    return render(request, "main/error.html")
