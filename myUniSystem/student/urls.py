
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name="student_home"),
    path('assessments/<int:id>', views.studentAssessments),
]
