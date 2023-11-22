from django.urls import path
from . import views


urlpatterns = [
    path("quizs/", views.QuizsView.as_view()),
    path("quizs/<uuid:quiz_id>/", views.QuizsDetailView.as_view()),
]
