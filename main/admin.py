from django.contrib import admin
from main.models import Contact, Profile
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('name', 'email', 'Mobile_no',
                 'Elaborate_Your_Concern', 'execution_time')


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('user', 'is_student', 'is_teacher', 'is_hod',
                 'is_director')
