from staff.models import Director, Hod, Staff, Teacher
from django.contrib import admin
from .models import Teacher, Hod
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'department',
                 'email', 'time', 'teacher_user')


@admin.register(Hod)
class HodAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'department',
                 'email', 'time', 'hod_user')


@admin.register(Director)
class DirectorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'department',
                 'email', 'time', 'director_user')

# only for inheritance
admin.site.register(Staff)
