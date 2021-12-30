from staff.models import StudentNote
from staff.views import attendance
from student.models import Book, Mark, Student, StudentAttendance, StudentClass
from main.models import Notice
from django.http.response import JsonResponse
from main.decoraters import student_only
from django.shortcuts import redirect, render
import datetime
import calendar
from .forms import BookForm

# Create your views here.


@student_only
def index(request):
    student = request.user.student
    dbg = attendance.objects.filter(semester=student.semester)
    print(dbg)
    # student.attendance
    return render(request, 'student/index.html')


@student_only
def showAttendance(request):
    sems = range(1, request.user.student.semester+1)
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    if request.GET.get('type', '') == 'api':
        sem = int(request.GET.get('sem', request.user.student.semester))
        month = int(request.GET.get('month', datetime.date.today().month))

        try:
            year = request.user.student.attendance.filter(
                student__user_id="0192CS181112", semester=5, date__month=12).first().date.year
        except:
            return JsonResponse([], safe=False)

        daysCount = calendar.monthrange(year, month)[1]

        data = {}
        count = 0
        for d in range(1, daysCount+1):
            try:
                data[str(d)] = (request.user.student.attendance.filter(
                    semester=sem, date__month=month, date__day=d).first().is_present)
            except:
                data[str(d)] = False
                count += 1

        if (count == daysCount):
            return JsonResponse([], safe=False)

        return JsonResponse({"attendance": data, "absent": count, "present": daysCount-count}, safe=False)

    return render(request, 'student/attendance.html', {"sem": sems, "month": months})


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
                return redirect('/student/library')
        else:
            form = BookForm()
        return render(request, 'student/add_book.html', {'form': form})
    else:
        return redirect('/login/')


# Update Books
@student_only
def updateBook(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return redirect('/student/library')
        else:
            pi = Book.objects.get(pk=id)
            form = BookForm(instance=pi)
        return render(request, 'student/update_book.html', {'form': form})
    else:
        return redirect('/login/')


# Delete Book
@student_only
def deleteBook(request, id):
    if request.user.is_authenticated:
        pi = Book.objects.get(pk=id)
        pi.delete()
        return redirect('/student/library')
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
    current_stu_sem = student.semester
    request.semesters = range(1, current_stu_sem+1)
    request.sem = request.GET.get('sem', current_stu_sem)
    if request.GET.get('req', '') == 'view':
        request.mark = student.mark.filter(semester=request.sem).first()
        return render(request, 'student/view-mark.html')
    request.marks = {}
    for sem in request.semesters:
        request.marks[str(sem)] = ""
        request.marks[str(sem)] = student.mark.filter(semester=sem).first()
    if request.GET.get('req', '') == 'add' or request.marks == None:
        return render(request, 'student/add-marks.html')

    return render(request, 'student/marks.html')


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
