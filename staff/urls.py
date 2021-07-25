from django.urls import path
from staff import views

urlpatterns = [
    # for all
    path('', views.index, name="s_Home"),
    path('attendance/', views.attendance, name="s_attendance"),
    path('attendance/view/', views.viewAttendance, name="s_view_attendance"),
    path('attendance/by-enrollments/', views.addAttendanceByEnroll,
         name="s_add_attendance_by_enroll"),

    # for notices
    path('notices/', views.viewAllNotices, name="view_notices"),
    path('notices/add/', views.addNotice, name="add_notice"),
    path('notices/<int:id>/', views.viewNotice, name="view_notice"),
    path('notices/<int:id>/update/', views.updateNotice, name="update_notice"),
    path('notices/<int:id>/delete/', views.deleteNotice, name="delete_notice"),

    # for notes
#     path('notes/', views.viewStaffNotes, name="view_staff_notes"),
    path('notes/add/', views.addNote, name="add_note"),
    path('notes/', views.viewAllNotesByStaff,
         name="view_staff_notes"),
    path('notes/<int:id>/', views.viewNote, name="view_note"),
    path('notes/<int:id>/update/', views.updateNote, name="update_note"),
    path('notes/<int:id>/delete/', views.deleteNote, name="delete_note"),
    path('students/', views.viewAllStudents, name="view_students"),
    path('students/<str:username>/',
         views.viewStudentProfile, name="view_student_profile"),
    
    # for teacher
    path('students/add', views.addStudent, name="t_add_student"),
    path('marks/', views.marks, name="t_marks"),

    # for hod
    path('add-teacher/', views.addTeacher, name="h_add_teacher"),

    # for director
    path('add-hod/', views.addHod, name="d_add_hod"),

    path('library/', views.library, name="library"),
    path('classes/', views.classes, name="classes"),
    path('classes/add/', views.addClasses, name="add_class"),
    path('classes/<int:id>/', views.updateClasses, name="update_class"),
    
    # academic calender's events
    path('events/', views.viewEvents, name="s_view_events"),
]
