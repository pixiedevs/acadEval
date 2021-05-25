from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name="studentHome"),
    path('attendance', views.showAttendance, name="showStudentAttendance"),
]
