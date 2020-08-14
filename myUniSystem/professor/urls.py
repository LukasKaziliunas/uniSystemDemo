from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home , name="professor_home"),
    path('subject/<int:subject_id>', views.subject_students),
    path('student_grades/<int:stud_id>/<int:subject_id>', views.student_grades),
    path('save_grades/<int:subject_id>', views.saveGrades)
]