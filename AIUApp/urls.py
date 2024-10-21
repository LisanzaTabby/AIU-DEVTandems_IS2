from django.urls import path
from .import views

urlpatterns  = [
    path('', views.index, name='home'),
    path('room/', views.rooms, name='room'),
]