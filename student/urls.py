from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name="studentHome"),
    path('attendance/', views.showAttendance, name="showStudentAttendance"),
    path('library/', views.library, name="library"),
    path('profile/', views.viewProfile, name="view_profile"),
    
    path('notes/', views.viewAllNotes, name="view_notes"),
    path('notes/<int:id>/', views.viewNote, name="view_note"),

    path('notices/', views.viewAllNotices, name="view_notices"),
    path('notices/<int:id>/', views.viewNotice, name="view_notice"),
]
