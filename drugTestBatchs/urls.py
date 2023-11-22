from django.urls import path
from . import views


urlpatterns = [
    path("drugTestBatchs/", views.DrugTestBatchsView.as_view()),
    path("drugTestBatchs/<uuid:drugTestBatch_id>/", views.DrugTestBatchsDetailView.as_view()),
]
