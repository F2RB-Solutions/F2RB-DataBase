from django.urls import path
from . import views


urlpatterns = [
    path("patients/", views.PatientsView.as_view()),
    path("patients/<uuid:patient_id>/", views.PatientsDetailView.as_view()),
]
