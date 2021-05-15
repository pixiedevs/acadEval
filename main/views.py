from django.http.response import HttpResponse
from django.shortcuts import render

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
    return render(request, "main/index.html")
    
# for login
def login(request):
    return render(request, "main/index.html")
