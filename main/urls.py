from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('help', views.help, name="help"),
    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
]
