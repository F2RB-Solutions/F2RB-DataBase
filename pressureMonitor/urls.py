from django.urls import path
from . import views


urlpatterns = [
    path("pressureMonitors/", views.PressureMonitorsView.as_view()),
    path("pressureMonitors/<uuid:pressureMonitor_id>/", views.PressureMonitorsDetailView.as_view()),
]
