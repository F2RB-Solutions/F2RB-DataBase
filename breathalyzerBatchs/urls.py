from django.urls import path
from . import views
urlpatterns = [
    path("breathalyzerBatchs/", views.BreathalyzerBatchsView.as_view()),
    path("breathalyzerBatchs/<uuid:breathalyzerBatch_id>/", views.BreathalyzerBatchsDetailView.as_view()),
]
