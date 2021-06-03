from main.resources import ContactResource
# from django.test import TestCase
from main.models import Contact
from django.contrib.auth.models import User
from student.models import Student
import json
# Create your tests here.

cr = ContactResource()
cr.import_data()



# u = User.objects.create(username=d['username'], password=d['password'])
# s = Student.objects.create(user=u, student_id=d['username'], first_name=d['first_name'],
                        #    email=d['email'], last_name=d['last_name'], batch_year=d['batch_year'], semester=d['semester'], year=d['year'], date_of_birth=d['date_of_birth'])

# x

# c2 = Contact.objects.create(id=d['id'], name=dl[1]['name'], email=dl[1]['email'], message=dl[1]['message'])



# sem = 6
# month = 5

# user = User.objects.get(username='pp')

# cs = user.student.get_attendance_by_sem_month(
#     sem=sem, month=month).values()
