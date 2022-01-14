from staff.models import StudentNote
from student.helper import predictMark
from student.models import Book, Mark, Student, StudentClass
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
    semester = request.user.student.semester
    dateData = request.user.student.attendance.filter(
        semester=semester).values_list('date__year', 'date__month').distinct()

    request.data = {}
    request.data["attendance"] = {"absent": 0,
                                  "present": 0, "monthly": [], "months": []}
    request.data["attendance"]["monthly"] = []

    for (year, month,) in dateData:
        daysCount = calendar.monthrange(year, month)[1]
        request.data["attendance"]["absent"] += daysCount
        attendance = request.user.student.attendance.filter(
            semester=semester, date__year=year, date__month=month).count()
        request.data["attendance"]["present"] += attendance

        request.data["attendance"]["months"].append([month, year])
        request.data["attendance"]["monthly"].append([daysCount, attendance])

    request.data["attendance"]["absent"] -= request.data["attendance"]["present"]

    request.data["marks"] = request.user.student.mark.filter(
        result='PASS').order_by("semester", '-id').values("semester", "sgpa")

    request.data["classes"] = StudentClass.objects.filter(
        branch__icontains=request.user.student.branch, semester=request.user.student.semester).order_by("-date")

    request.data["notices"] = Notice.objects.filter(
        branch=request.user.student.branch).order_by("-modified_at")

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


@student_only
def viewProfile(request):
    student = request.user.student
    return render(request, 'student/profile.html', {"student": student})


@student_only
def updateProfile(request):
    if request.method == 'POST':
        if request.POST.get('father_name', '') != '':
            request.user.student.father_name = request.POST.get(
                'father_name', '')
        if request.POST.get('mobile_no', '') != '':
            request.user.student.mobile_no = request.POST.get('mobile_no', '')
        if request.POST.get('father_mobile_no', '') != '':
            request.user.student.father_mobile_no = request.POST.get(
                'father_mobile_no', '')
        if request.POST.get('permanent_address', '') != '':
            request.user.student.permanent_address = request.POST.get(
                'permanent_address', '')
        if request.POST.get('current_address', '') != '':
            request.user.student.current_address = request.POST.get(
                'current_address', '')
        if request.POST.get('guardian_name', '') != '':
            request.user.student.guardian_name = request.POST.get(
                'guardian_name', '')
        if request.POST.get('guardian_mobile_no', '') != '':
            request.user.student.guardian_mobile_no = request.POST.get(
                'guardian_mobile_no', '')
        request.user.student.save()

    return redirect('view_profile')


# for student notes made/provided by teachers
@student_only
def viewNote(request, id):
    note = StudentNote.objects.get(id=id)
    return render(request, 'staff/view-note.html', {"data": note, "dataName": "note"})


@student_only
def viewAllNotes(request):
    notes = StudentNote.objects.filter(
        branch=request.user.student.branch).order_by("-modified_at")
    return render(request, 'staff/view-all-notices.html', {"data": notes, "dataName": "note"})


# for student notice created by staff
@student_only
def viewAllNotices(request):
    notices = Notice.objects.filter(
        branch=request.user.student.branch).order_by("-modified_at")
    return render(request, "staff/view-all-notices.html", {"data": notices, "dataName": "notice"})


@student_only
def viewNotice(request, id):
    notice = Notice.objects.get(id=id)
    return render(request, "staff/view-notice.html", {"data": notice, "dataName": "notice"})


def StudentClasses(request):
    request.data = StudentClass.objects.filter(
        branch__icontains=request.user.student.branch, semester=request.user.student.semester).order_by("-date")
    return render(request, 'student/classes.html')


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

    marks = student.mark.values_list('sgpa')
    prediction = predictMark([m[0] for m in marks])
    request.prediction = prediction

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

    return redirect("/student/marks/")
