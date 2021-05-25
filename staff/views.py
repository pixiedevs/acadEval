from django.shortcuts import render
from student.forms import AddStudentForm, StudentRegisterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from staff.forms import AddTeacherForm, TeacherDataForm
from staff.forms import AddHodForm, HodDataForm

# Create your views here.


def index(request):
    return render(request, 'staff/index.html')


def attendance(request):
    return render(request, 'staff/attendance.html')


def marks(request):
    return render(request, 'staff/marks.html')


def library(request):
    return render(request, 'staff/library.html')


def classes(request):
    return render(request, 'staff/classes.html')


# this method for add student by vishal
def addStudent(request):

    if request.method == 'POST':
        asform = AddStudentForm(request.POST)
        srform = StudentRegisterForm(request.POST)
        if asform.is_valid() and srform.is_valid():
            user = asform.save()
            user.set_password(user.password)
            user.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
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


def addTeacher(request):
    if request.method == 'POST':
        atform = AddTeacherForm(data=request.POST)
        tdform = TeacherDataForm(data=request.POST)
        if atform.is_valid() and tdform.is_valid():
            teacher_user = atform.save()
            teacher_user.set_password(teacher_user.password)
            teacher_user.save()
            group = Group.objects.get(name='teacher')
            teacher_user.groups.add(group)
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


def addHod(request):
    if request.method == 'POST':
        ahform = AddHodForm(data=request.POST)
        hdform = HodDataForm(data=request.POST)
        if ahform.is_valid() and hdform.is_valid():
            hod_user = ahform.save()
            hod_user.set_password(hod_user.password)
            hod_user.save()
            group = Group.objects.get(name='hod')
            hod_user.groups.add(group)
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
