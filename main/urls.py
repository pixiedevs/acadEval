from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('help', views.help, name="help"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginHandle, name="login"),
    path('logout', views.logOutHandle, name="logout"),
    path('dashboard', views.dashboardAsType, name="dashboard"),
    path('test', views.test, name="test"),
]
