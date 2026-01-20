# monitor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.server_status),
]
