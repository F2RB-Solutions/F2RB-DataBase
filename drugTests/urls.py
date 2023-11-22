from django.urls import path
from . import views


urlpatterns = [
    path("drugTests/", views.DrugTestsView.as_view()),
    path("drugTests/<uuid:drugTest_id>/", views.DrugTestsDetailView.as_view()),
]
