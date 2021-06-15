from staff.models import StudentNote
from student.models import Book, Student
from main.models import Notice
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


# library views
@student_only
def library(request):
    books = request.user.student.book.all()
    return render(request, 'student/studentLibrary.html', {"books": books})


# for student notes made/provided by teachers
@student_only
def viewProfile(request):
    student = request.user.student
    return render(request, 'student/profile.html', {"student": student})


# for student notes made/provided by teachers
@student_only
def viewNote(request, id):
    note = StudentNote.objects.get(id=id)
    return render(request, 'staff/view-notice.html', {"data": note, "dataName": "note"})


@student_only
def viewAllNotes(request):
    notes = sorted(StudentNote.objects.filter(
        branch=request.user.student.branch), key=lambda x: x.modified_at.date(), reverse=True)
    return render(request, 'staff/view-all-notices.html', {"data": notes, "dataName": "note"})


# for student notice created by staff
@student_only
def viewAllNotices(request):
    notices = sorted(Notice.objects.filter(
        branch=request.user.student.branch), key=lambda x: x.modified_at.date(), reverse=True)
    return render(request, "staff/view-all-notices.html", {"data": notices, "dataName": "notice"})


@student_only
def viewNotice(request, id):
    notice = Notice.objects.get(id=id)
    return render(request, "staff/view-notice.html", {"data": notice, "dataName": "notice"})


def StudentClasses(request):
    d = Book.objects.all()
    return render(request, 'student/classes.html', {"data": d, "dataName": "Class"})


@student_only
def showMarks(request):
    semesters = range(1, request.user.student.semester+1)
    student = Student.objects.get(user=request.user)
    marks = student.mark.get(semester=student.semester)
    return render(request, 'student/marks.html', {"semesters": semesters, "marks": marks})
