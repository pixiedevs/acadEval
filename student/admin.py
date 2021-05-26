from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('first_name', 'last_name', 'branch',
                 'email', 'batch_year', 'time', 'user')
