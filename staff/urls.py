from django.urls import path
from staff import views

urlpatterns = [
    path('', views.index, name="home"),
    # path('', views.index, name="home"),
]
