from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('details/', views.blog_details_view, name='blog_details_view'),
]