from django.urls import path
from . import views


urlpatterns = [
    path("breathalyzerTests/", views.BreathalyzerTestsView.as_view()),
    path("breathalyzerTests/<uuid:breathalyzerTest_id>/", views.BreathalyzerTestsDetailView.as_view()),
]
