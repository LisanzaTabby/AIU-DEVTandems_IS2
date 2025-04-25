from django.urls import path
from .import views

urlpatterns  = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('register/', views.registerPage, name='register'),

    path('', views.index, name='home'),
    path('room/<str:pk>/', views.rooms, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    
    path('create-room/', views.create_room, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='updateroom'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='deleteroom'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('updateUser/', views.updateUser, name='update-user'),
]