from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
 list_display = ('name', 'email', 'Mobile_no',
                 'Elaborate_Your_Concern', 'execution_time')
