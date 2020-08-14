from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.index),
   path('ajax/load_week/', views.week_timetable, name="ajax_load_timetable"),
   path('makeNew/', views.make_timetableEntry, name="name_new_timetable")
]
