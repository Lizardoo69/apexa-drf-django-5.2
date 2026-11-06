from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team_view, name='team'),
    path('details/', views.team_details_view, name='team_details'),
]