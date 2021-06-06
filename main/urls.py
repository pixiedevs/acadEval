from django.urls import path, include
from main import apiview, views
from django.contrib.auth import views as auth_views
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

    # password reset urls
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="main/registrations/password_reset_form.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="main/registrations/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="main/registrations/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name="main/registrations/password_reset_complete.html"), name='password_reset_complete'),
]
