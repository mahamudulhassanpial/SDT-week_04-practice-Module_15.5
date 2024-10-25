# music/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('musicians/', views.musician_list, name='musician_list'),
    path('musicians/add/', views.musician_create, name='musician_create'),
    path('musicians/edit/<int:pk>/', views.musician_edit, name='musician_edit'),
    path('musicians/delete/<int:pk>/', views.musician_delete, name='musician_delete'),
    
    path('albums/', views.album_list, name='album_list'),
    path('albums/add/', views.album_create, name='album_create'),
    path('albums/edit/<int:pk>/', views.album_edit, name='album_edit'),
    path('albums/delete/<int:pk>/', views.album_delete, name='album_delete'),
]
