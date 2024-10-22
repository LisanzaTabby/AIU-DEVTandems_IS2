from django.urls import path
from .import views

urlpatterns  = [
    path('', views.index, name='home'),
    path('room/<str:pk>/', views.rooms, name='room'),
]