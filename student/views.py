from staff.models import StudentNote
from student.models import Book, Mark, Student, StudentClass
from main.models import Notice
from django.http.response import JsonResponse
from main.decoraters import student_only
from django.shortcuts import redirect, render
from datetime import datetime
from .forms import BookForm

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


@student_only
def addBook(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BookForm(request.POST)
            new_book = Book()
            if form.is_valid():
                new_book.book_id = form.cleaned_data['book_id']
                new_book.book_name = form.cleaned_data['book_name']
                new_book.issue_date = form.cleaned_data['issue_date']
                new_book.expiry_date = form.cleaned_data['expiry_date']
                new_book.student = request.user.student
                new_book.save()
                form = BookForm()
        else:
            form = BookForm()
        return render(request, 'student/add_book.html', {'form': form})
    else:
        return redirect('/login/')


# Update Books
def updateBook(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Book.objects.get(pk=id)
            form = BookForm(instance=pi)
        return render(request, 'student/update_book.html', {'form': form})
    else:
        return redirect('/login/')

# Delete Book


def deleteBook(request, id):
    if request.user.is_authenticated:
        pi = Book.objects.get(pk=id)
        pi.delete()
        return render(request, 'student/studentLibrary.html')
    else:
        return redirect('/login/')


# for student notes made/provided by teachers
@student_only
def viewProfile(request):
    student = request.user.student
    return render(request, 'student/profile.html', {"student": student})


# for student notes made/provided by teachers
@student_only
def viewNote(request, id):
    note = StudentNote.objects.get(id=id)
    return render(request, 'staff/view-note.html', {"data": note, "dataName": "note"})


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
    data = sorted(StudentClass.objects.filter(
        branch__icontains=request.user.student.branch, semester=request.user.student.semester), key=lambda x: x.date, reverse=True)
    return render(request, 'student/classes.html', {"data": data, "dataName": "Class"})


@student_only
def showMarks(request):
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        semester = request.POST['sem']
        print(semester)
        try:
            marks = student.mark.get(semester=semester)
            
        except:
            return render(request, 'student/add-marks.html', {"sem": semester})

    else:
        marks = student.mark.get(semester=student.semester)
        
    semesters = range(1, request.user.student.semester+1)
    return render(request, 'student/marks.html', {"semesters": semesters, "marks": marks})


@student_only
def addMarks(request):
    if request.method == 'POST':
        mark = Mark()
        mark.student = request.user.student
        mark.semester = request.POST['semester']
        mark.cgpa = request.POST['cgpa']
        mark.sgpa = request.POST['sgpa']
        mark.result = request.POST['result'].upper()
        mark.file = request.FILES['file']
        mark.save()
        
        marks = request.user.student.mark.get(
            semester=request.user.student.semester)
        semesters = range(1, request.user.student.semester+1)
        return render(request, 'student/marks.html', {"semesters": semesters, "marks": marks})
    return redirect("/")
    # return render(request, 'student/marks.html')
