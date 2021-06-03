from main.decoraters import director_only, hod_only, staff_only, teacher_only
from student.forms import AddStudentForm, StudentRegisterForm
from django.shortcuts import redirect, render
from student.models import Student
from main.models import Notice
from django.contrib import messages
from django.contrib.auth.models import Group
from staff.forms import AddTeacherForm, TeacherDataForm
from staff.forms import AddHodForm, HodDataForm

# Create your views here.


@staff_only
def index(request):
    return render(request, 'staff/index.html')



@staff_only
def attendance(request):
    return render(request, 'staff/attendance.html')


@staff_only
def marks(request):
    return render(request, 'staff/marks.html')


@staff_only
def library(request):
    return render(request, 'staff/library.html')


@staff_only
def classes(request):
    return render(request, 'staff/classes.html')


# this method for add student by vishal
@teacher_only
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
                request, 'Congratulation! You have registed successfully!!')
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
                request, 'Congratulation! You have registed successfully!!')
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
                request, 'Congratulation! You have registed successfully!!')
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
    notices = Notice.objects.all()
    return render(request, "staff/view-all-notices.html", {"notices": notices})

@staff_only
def viewNotice(request, id):
    notice = Notice.objects.filter(id=id).first()
    return render(request, "staff/view-notice.html", {"notice": notice})


@staff_only
def deleteNotice(request, id):
    notice = Notice.objects.get(id=id)
    if notice.created_by == request.user:
        notice.delete()
        messages.success(request, f"Notice with {id} has been deleted")
        return redirect('view_notices')

    messages.error(request, "You do not permition to delete this notice.")
    return redirect(f'/staff/notices/{id}')


@staff_only
def addNotice(request):
    if request.method == 'POST':
        notice = Notice.objects.create(
            created_by=request.user, title=request.POST['title'], content=request.POST['content'])
        return redirect(f'/staff/notices/{notice.id}')
    else:
        return render(request, 'staff/add-notice.html')
    
    
@staff_only
def updateNotice(request, id):
    notice = Notice.objects.get(id=id)
    if request.method == 'POST':
        Notice.objects.update(
            created_by=request.user, title=request.POST['title'], content=request.POST['content'])
        return redirect(f'/staff/notices/{notice.id}')

    else:
        return render(request, 'staff/add-notice.html', {"notice": notice},)
        

# views for Student's data
@staff_only
def viewAllStudents(request):
    students = Student.objects.filter(branch=request.user.teacher.department)
    return render(request, "staff/view-all-students.html", {"students": students})


@staff_only
def viewStudentProfile(request, username):
    student = Student.objects.get(user=username, branch=request.user.teacher.department)
    return render(request, "student/profile.html", {"student": student})
