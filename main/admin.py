from django.contrib import admin
from main.models import Contact, Notice, Profile
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('name', 'email', 'mobile_no',
                 'message', 'time')


@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('user', 'is_student', 'is_teacher', 'is_hod',
                 'is_director')


@admin.register(Notice)
class NoticeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
 list_display = ('title', 'created_at', 'modified_at')
