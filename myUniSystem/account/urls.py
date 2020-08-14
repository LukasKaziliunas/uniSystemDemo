from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.registration_page),
    path('login/', views.login_page),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', views.redirect_home, name="user_home"),
    path('createCourses/', views.createStudentCourses)
]
