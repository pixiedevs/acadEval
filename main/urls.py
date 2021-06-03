from django.urls import path, include
from main import apiview, views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('contact', apiview.ContactViewSet, basename='contact')

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('help', views.help, name="help"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginHandle, name="login"),
    path('logout', views.logOutHandle, name="logout"),
    path('dashboard', views.dashboardAsType, name="dashboard"),
    path('test', views.test, name="test"),
    # for js only
    # path('api/', include(router.urls)),
    path('api/<slug>', apiview.contact_view),
]
