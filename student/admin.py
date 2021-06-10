from django.contrib import admin
from .models import Book, Mark, Student, StudentAttendance, StudentClass
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


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ('student', 'book_id', 'book_name', 'issue_date',
                 'expiry_date')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
 list_display = ('student', 'result', 'sgpa', 'cgpa')


@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
 list_display = ('subject', 'tutor', 'start_time', 'end_time', 'date')
