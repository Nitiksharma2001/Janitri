from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.getPatientsOfDoctor),
    path('patient/<int:patient_id>', views.patientOfDoctor)
]
