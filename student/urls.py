from django.urls import path
from student import views

urlpatterns = [
    path('', views.index, name="studentHome"),
    path('attendance/', views.showAttendance, name="showStudentAttendance"),
    path('marks/', views.showMarks, name="showStudentMarks"),
    path('marks/add/', views.addMarks, name="addStudentMarks"),
    path('classes/', views.StudentClasses, name="all_classes"),
    path('profile/', views.viewProfile, name="view_profile"),
    
    path('notes/', views.viewAllNotes, name="view_notes"),
    path('notes/<int:id>/', views.viewNote, name="view_note"),

    path('notices/', views.viewAllNotices, name="view_notices"),
    path('notices/<int:id>/', views.viewNotice, name="view_notice"),

    # Books
    path('library/', views.library, name="library"),
    path('add-book/', views.addBook, name='add_book'),
    path('update-book/<int:id>/', views.updateBook, name='update_book'),
    path('delete-book/<int:id>/', views.deleteBook, name='delete_book'),
]
