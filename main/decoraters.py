from django.shortcuts import redirect
# from django.contrib.auth.models import User


def auth_req(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func


def unauth_req(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return views_func(request, *args, **kwargs)
    return wrapper_func


# def from_college(views_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.is_active and (request.user.is_superuser or request.user.profile.type is not "visitor"):
#             return views_func(request, *args, **kwargs)
#         else:
#             return redirect('home')
#     return wrapper_func


def student_only(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active and request.user.profile.is_student:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func


def staff_only(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active and (request.user.profile.is_director or request.user.profile.is_hod or request.user.profile.is_teacher):
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func


def teacher_only(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active and request.user.profile.is_teacher:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func


def hod_only(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active and request.user.profile.is_hod:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func


def director_only(views_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_active and request.user.profile.is_director:
            return views_func(request, *args, **kwargs)
        else:
            return redirect('home')
    return wrapper_func
