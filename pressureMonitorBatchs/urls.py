from django.urls import path
from . import views


urlpatterns = [
    path("pressureMonitorBatchs/", views.PressureMonitorBatchsView.as_view()),
    path("pressureMonitorBatchs/<uuid:pressureMonitorBatch_id>/", views.PressureMonitorBatchsDetailView.as_view()),
]
