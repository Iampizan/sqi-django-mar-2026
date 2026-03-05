from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('profile-page', views.profile_page, name='profile_page'),
    path('service-page', views.service_page, name='service_page'),
    path('help-page', views.help_page, name='help_page'),
]