# from django.http.response import HttpResponse
from django.shortcuts import render #, HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, 'student/index.html')

