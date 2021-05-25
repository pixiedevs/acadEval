from django.urls import path
from staff import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-student', views.addStudent, name="add_student"),
    path('add_teacher', views.addTeacher, name="add_teacher"),
    path('add_hod', views.addHod, name="add_hod"),

    path('attendance', views.attendance, name="attendance"),
    path('marks', views.marks, name="marks"),
    path('library', views.library, name="library"),
    path('classes', views.classes, name="classes"),
    # path('', views.index, name="home"),
]
