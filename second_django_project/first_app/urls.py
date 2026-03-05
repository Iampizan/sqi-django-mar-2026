from django.urls import path
from . import views

urlpatterns = [
    path("correct-code", views.corect_code, name="correct_code"),
    path("incorrect-code", views.not_correct_code, name="not_correct_code"),
]