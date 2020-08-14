
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajax/load_fields/', views.load_fields, name='ajax_load_fields'),
    path('field/<int:id>', views.field_info),
]
