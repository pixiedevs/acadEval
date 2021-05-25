from django.contrib import admin
from main.models import Contact, Profile
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
 list_display = ('name', 'email', 'Mobile_no',
                 'Elaborate_Your_Concern', 'execution_time')


admin.site.register(Profile)
