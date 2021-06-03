from django.contrib import admin
from .models import Student, StudentAttendance
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('user', 'first_name', 'last_name', 'branch',
                 'email', 'batch_year', 'time')

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('student', 'semester', 'date',
                 'is_present')
