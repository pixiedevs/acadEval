# from django.http.response import HttpResponse
from django.shortcuts import redirect, render #, HttpResponseRedirect

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.profile.type() == "student":
            return render(request, 'student/index.html')
    return redirect('home')


def showAttendance(request):
    if request.user.is_authenticated:
        if request.user.profile.type() == "student":
            sem = range(1, 7)
            month = ['jan', "fab"]
            return render(request, 'student/attendance.html', {"sem": sem, "month": month})
    return redirect('home')

