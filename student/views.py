from django.http.response import JsonResponse
from main.decoraters import student_only
from django.shortcuts import render
from datetime import datetime
# Create your views here.


@student_only
def index(request):
    return render(request, 'student/index.html')


@student_only
def showAttendance(request):
    sems = range(1, request.user.student.semester+1)
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if request.method == 'POST':
        sem = request.POST['sem']
        month = request.POST['month']
        data = request.user.student.get_attendance_by_sem_month(
            sem=sem, month=month).values()
        return JsonResponse(list(data), safe=False)


    return render(request, 'student/attendance.html', {"sem": sems, "month": months[:datetime.now().month]})
