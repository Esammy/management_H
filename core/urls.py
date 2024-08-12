# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('patients/staff/<int:id>/', views.patients_by_staff, name='patients_by_staff'),
    path('patients/discharged/', views.discharged_patients, name='discharged_patients'),
    path('admissions/day/', views.day_with_most_admissions, name='day_with_most_admissions'),
    path('patients/staff/avg_duration/', views.avg_duration_by_staff, name='avg_duration_by_staff'),
]
