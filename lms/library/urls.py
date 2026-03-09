from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
] 