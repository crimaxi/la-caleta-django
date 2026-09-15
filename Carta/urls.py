from django.urls import path

from . import views

app_name = 'Carta'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('platos/', views.inicio, name='lista'),
]