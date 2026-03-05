from django.urls import path
from . import views

urlpatterns = [
    path("correct-code", views.second_correct_code, name="second_correct_code"),
    path("incorrect-code", views.second_incorrect_code, name="second_incorrect_code"),
]