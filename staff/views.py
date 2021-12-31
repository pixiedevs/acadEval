import xlwt
from django.db.models.expressions import F
from main.decoraters import director_only, hod_only, staff_only
from student.forms import AddStudentForm, StudentRegisterForm
from django.shortcuts import redirect, render
from student.models import Student, Mark, StudentAttendance, StudentClass
from main.models import Notice
from staff.models import StudentNote
from django.contrib import messages
from django.contrib.auth.models import Group
from staff.forms import AddTeacherForm, TeacherDataForm, AddHodForm, HodDataForm
import datetime
from main.resources import StudentAttendanceResource
from django.http.response import HttpResponse
from django.db.models import Count
# Create your views here.


@staff_only
def index(request):
    return render(request, 'staff/index.html')


@staff_only
def viewProfile(request):
    staff = request.user.profile.staff
    return render(request, 'staff/profile.html', {"staff": staff})


@staff_only
def attendance(request):
    branches = "CSE, IT, ECE, ME, CE"
    data = {"branches": branches.split(", "), "semesters": range(1, 9)}

    return render(request, 'staff/insert-attendance.html', {"data": data})


@staff_only
def viewAttendance(request):
    branches = "CSE, IT, ECE, ME, CE"
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    branch = request.GET.get("branch", request.user.profile.staff.department)
    semester = request.GET.get("semSelect", 6)
    export = bool(request.GET.get("export", False))

    fromDate = request.GET.get("fromDate", datetime.date.min)
    toDate = request.GET.get("toDate", datetime.date.today())

    attendance = (StudentAttendance.objects.filter(semester=semester, is_present=True, date__gte=fromDate if fromDate != "" else datetime.date.min,
                    date__lte=toDate if toDate != "" else datetime.date.today()).annotate(enrollment=F("student__user")).values_list("enrollment").annotate(attendance=Count("is_present")).order_by())

    if export:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f'attachment; filename="attendance-sem{semester}-{datetime.date.today()}.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Attendance')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['student', 'attendance']

        for col in range(len(columns)):
            ws.write(row_num, col, columns[col], font_style)

        font_style = xlwt.XFStyle()

        for row in attendance:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response
    data = {"branches": branches.split(", "), "semesters": range(1, 9), "attendance": attendance,
            "branch": branch, "semester": semester, "months": months, "toDate": toDate, "fromDate": fromDate}

    return render(request, 'staff/all-students-attendance.html', {"data": data})


@staff_only
def addAttendanceByEnroll(request):
    error_info = ""
    if request.method == 'POST':
        enrolls = request.POST["EnrollInput"].upper()
        semester = request.POST["semesterInput"]
        date = request.POST["dateInput"]
        present = bool(request.POST.get("presentInput", "off"))

        enrolls = enrolls.split(", ")
        if(len(enrolls) == 1):
            enrolls = enrolls[0].split(",")

        enrolls_count = len(enrolls)

        for enroll in enrolls:
            try:
                if request.user.profile.is_director:
                    student = Student.objects.get(user=enroll)
                else:
                    student = Student.objects.get(
                        branch=request.user.profile.staff.department, user=enroll)
                StudentAttendance.objects.update_or_create(
                    student=student, semester=semester, date=date, is_present=present)
            except:
                error_info += (enroll+", ")
                enrolls_count -= 1
                # messages.ERROR(request, "There is a problem with adding attendance!")

        messages.success(
            request, f'Attendance of {enrolls_count} students has been added successfully.\n{error_info if len(error_info) != 0 else ""}')

    else:
        messages.ERROR(request, "There is a problem with adding attendance!")

    return redirect("s_attendance")


@staff_only
def marks(request):
    branches = "CSE, IT, ECE, ME, CE"
    semesters = range(1, 9)
    # if request.user.profile.is_director:
    #     branch = request.GET.get("branchSelect", request.user.profile.staff.department)
    # else:
    #     branch = request.user.profile.staff.department
    branch = request.GET.get(
        "branchSelect", request.user.profile.staff.department)

    semester = request.GET.get("semSelect", 6)

    marks = Mark.objects.filter(
        student__branch__contains=branch, semester=semester)

    data = {}
    data["marks"] = marks
    data["semester"] = semester
    data["semesters"] = semesters
    data["branch"] = branch
    data["branches"] = branches.split(", ")

    return render(request, 'staff/all-students-marks.html', {"data": data})


@staff_only
def library(request):
    return render(request, 'staff/library.html')


@staff_only
def classes(request):

    data = sorted(StudentClass.objects.filter(
        branch__icontains=request.user.profile.staff.department), key=lambda x: x.date, reverse=True)
    return render(request, 'staff/classes.html', {"data": data, "dataName": "Class"})


@staff_only
def addClasses(request):
    branches = "CSE, IT, ECE, ME, CE"
    if request.method == 'POST':
        studentClass = StudentClass()
        studentClass.subject = request.POST['subject']
        branch = request.POST['branch'].upper()

        if branch == "ALL":
            branch = branches
        studentClass.branch = branch

        studentClass.semester = request.POST['semester']
        studentClass.url = request.POST['class_url']
        studentClass.start_time = request.POST['start_time']
        studentClass.end_time = request.POST['end_time']
        studentClass.date = request.POST['date']
        studentClass.tutor = request.user
        studentClass.save()

        messages.success(
            request, f'{studentClass.subject} class has been added successfully.')
        return redirect("classes")

    return render(request, 'staff/add-class.html')


@staff_only
def updateClasses(request, id):
    branches = "CSE, IT, ECE, ME, CE"
    studentClass = StudentClass.objects.get(id=id)
    if request.user.profile.has_permission(studentClass.tutor):
        if request.method == 'POST':
            studentClass.subject = request.POST['subject']
            branch = request.POST['branch'].upper()

            if branch == "ALL":
                branch = branches
            studentClass.branch = branch

            studentClass.semester = request.POST['semester']
            studentClass.url = request.POST['class_url']
            studentClass.start_time = request.POST['start_time']
            studentClass.end_time = request.POST['end_time']
            studentClass.date = request.POST['date']
            studentClass.save()

            messages.success(
                request, f'{studentClass.subject} class has been added successfully.')
            return redirect("classes")
        return render(request, 'staff/update-class.html', {"studentClass": studentClass})

    else:
        messages.error(
            request, "You do not have permition to update this class.")

    return redirect("classes")


# this method for add student by vishal
@staff_only
def addStudent(request):

    if request.method == 'POST':
        asform = AddStudentForm(request.POST)
        srform = StudentRegisterForm(request.POST)
        if asform.is_valid() and srform.is_valid():
            user = asform.save()
            user.set_password(user.password)
            user.save()
            group, created = Group.objects.get_or_create(name='student')
            user.groups.add(group)
            user.profile.is_student = True
            user.save()
            profile = srform.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(
                request, 'Congratulation! You have registed successfully.')
            asform = AddStudentForm()
            srform = StudentRegisterForm()
        # else:
        #     HttpResponse("<h1>Somthing is Wrong</h1>")
    else:
        asform = AddStudentForm(request.POST)
        srform = StudentRegisterForm(request.POST)
    return render(request, 'staff/add-student.html', {'asform': asform, 'srform': srform})


# this method for add teacher  by vishal
@hod_only
def addTeacher(request):
    if request.method == 'POST':
        atform = AddTeacherForm(data=request.POST)
        tdform = TeacherDataForm(data=request.POST)
        if atform.is_valid() and tdform.is_valid():
            teacher_user = atform.save()
            teacher_user.set_password(teacher_user.password)
            teacher_user.save()
            group, created = Group.objects.get_or_create(name='teacher')
            teacher_user.groups.add(group)
            teacher_user.profile.is_teacher = True
            teacher_user.save()
            teacher_profile = tdform.save(commit=False)
            teacher_profile.teacher_user = teacher_user
            teacher_profile.save()
            messages.success(
                request, 'Congratulation! You have registed successfully.')
            atform = AddTeacherForm()
            tdform = TeacherDataForm()
        # else:
        #     HttpResponse("<h1>Somthing is Wrong</h1>")
    else:
        atform = AddTeacherForm(data=request.POST)
        tdform = TeacherDataForm(data=request.POST)
    return render(request, 'staff/add_teacher.html', {'atform': atform, 'tdform': tdform})


# this method for add teacher by vishal
@director_only
def addHod(request):
    if request.method == 'POST':
        ahform = AddHodForm(data=request.POST)
        hdform = HodDataForm(data=request.POST)
        if ahform.is_valid() and hdform.is_valid():
            hod_user = ahform.save()
            hod_user.set_password(hod_user.password)
            hod_user.save()
            group, created = Group.objects.get_or_create(name='hod')
            hod_user.groups.add(group)
            hod_user.profile.is_hod = True
            hod_user.save()
            hod_profile = hdform.save(commit=False)
            hod_profile.hod_user = hod_user
            hod_profile.save()
            messages.success(
                request, 'Congratulation! You have registed successfully.')
            ahform = AddHodForm()
            hdform = HodDataForm()
        # else:
        #     HttpResponse("<h1>Somthing is Wrong</h1>")
    else:
        ahform = AddHodForm(data=request.POST)
        hdform = HodDataForm(data=request.POST)
    return render(request, 'staff/add_hod.html', {'ahform': ahform, 'hdform': hdform})


# views for notice
@staff_only
def viewAllNotices(request):
    notices = sorted(Notice.objects.filter(
        branch=request.user.profile.staff.department), key=lambda x: x.modified_at.date(), reverse=True)
    return render(request, "staff/view-all-notices.html", {"data": notices, "dataName": "notice"})


@staff_only
def viewNotice(request, id):
    notice = Notice.objects.filter(id=id).first()
    return render(request, "staff/view-notice.html", {"data": notice, "dataName": "notice"})


@staff_only
def deleteNotice(request, id):
    notice = Notice.objects.get(id=id)
    if notice.created_by == request.user:
        notice.delete()
        messages.success(request, f"Notice with {id} has been deleted")
        return redirect('view_notices')

    messages.error(request, "You do not have permition to delete this notice.")
    return redirect(f'/staff/notices/{id}')


@staff_only
def addNotice(request):
    if request.method == 'POST':
        notice = Notice.objects.create(
            created_by=request.user, title=request.POST['title'], content=request.POST['content'], branch=request.user.profile.staff.department)
        return redirect(f'/staff/notices/{notice.id}')
    else:
        return render(request, 'staff/add-notice.html')


@staff_only
def updateNotice(request, id):
    notice = Notice.objects.get(id=id)
    if notice.created_by == request.user:
        if request.method == 'POST':
            Notice.objects.update(
                created_by=request.user, title=request.POST['title'], content=request.POST['content'])
            return redirect(f'/staff/notices/{notice.id}')

        else:
            return render(request, 'staff/add-notice.html', {"data": notice},)
    messages.error(request, "You do not have permition to update this notice.")
    return redirect(f'/staff/notices/{id}')


# views for notes
"""
Currently method viewStaffNotes is not in use
because of teacher's note's privacy
but it will be available for hod and director in the future
"""


@staff_only
def viewStaffNotes(request):
    staff = StudentNote.objects.values_list(
        'created_by').order_by('created_by').distinct()
    return render(request, "staff/view-all-staff.html", {"staff": staff, "dataName": "Teacher"})


@staff_only
def viewAllNotesByStaff(request):
    notes = sorted(StudentNote.objects.filter(created_by=request.user),
                   key=lambda x: x.modified_at.date(), reverse=True)

    if notes is None or len(notes) == 0:
        return redirect('add_note')
    return render(request, "staff/view-all-notes.html", {"data": notes, "dataName": "note"})


@staff_only
def viewNote(request, id):
    note = StudentNote.objects.filter(id=id).first()
    if note is None:
        return redirect(f'/staff/notes/')
    else:
        return render(request, "staff/view-note.html", {"data": note, "dataName": "note"})


@staff_only
def deleteNote(request, id):
    note = StudentNote.objects.get(id=id)
    if note.created_by == request.user:
        note.delete()
        messages.success(request, f"note with ID: {id} has been deleted")
        return redirect('view_staff_notes')

    messages.error(request, "You do not have permition to delete this notice.")
    return redirect(f'/staff/notes/{id}/')


@staff_only
def addNote(request):
    if request.method == 'POST':
        files = request.FILES['file']

        note = StudentNote.objects.create(
            created_by=request.user, topic=request.POST['topic'], subject=request.POST['subject'], branch=request.user.profile.staff.department)

        if files is not None:
            note.files = files
        content = request.POST['content']
        if content is not None or content != "":
            note.content = content
        note.save()

        return redirect(f'/staff/notes/{note.id}/')
    else:
        return render(request, 'staff/add-note.html', {"dataName": "note"})


@staff_only
def updateNote(request, id):
    note = StudentNote.objects.get(id=id)
    if note is None:
        return redirect(f'/staff/notes/')
    if note.created_by == request.user:
        if request.method == 'POST':
            note.topic = request.POST['topic']
            note.subject = request.POST['subject']
            note.content = request.POST['content']
            note.save()
            return redirect(f'/staff/notes/{note.id}/')

        else:
            return render(request, 'staff/add-note.html', {"data": note, "dataName": "note"})
    messages.error(request, "You do not have permition to update this note.")
    return redirect(f'/staff/notes/{id}/')


# views for Student's data
@staff_only
def viewAllStudents(request):
    students = Student.objects.filter(
        branch=request.user.profile.staff.department)
    return render(request, "staff/view-all-students.html", {"students": students})


@staff_only
def viewStudentProfile(request, username):
    student = Student.objects.get(
        user=username, branch=request.user.profile.staff.department)
    return render(request, "student/profile.html", {"student": student})


@staff_only
def viewEvents(request):
    return render(request, 'staff/view-all-events.html')
