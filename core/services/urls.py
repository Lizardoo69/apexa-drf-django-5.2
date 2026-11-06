from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services_view, name='services'),
    path('project-details/', views.services_details_view, name='project_details_view'),
]