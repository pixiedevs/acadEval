from django.contrib import admin
from .models import Teacher, Hod
# Register your models here.


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'department',
                 'email', 'time', 'teacher_user')


@admin.register(Hod)
class HodAdmin(admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'department',
                 'email', 'time', 'hod_user')
