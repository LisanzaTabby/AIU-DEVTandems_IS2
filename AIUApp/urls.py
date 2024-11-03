from django.urls import path
from .import views

urlpatterns  = [
    path('', views.index, name='home'),
    path('room/<str:pk>/', views.rooms, name='room'),
    path('create-room/', views.create_room, name='create-room'),
]