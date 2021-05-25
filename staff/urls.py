from django.urls import path
from staff import views

urlpatterns = [
    path('', views.index, name="staffHome"),
    path('add-student/', views.addStudent, name="add student"),
    # path('', views.index, name="home"),
]
