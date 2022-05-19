from django.contrib import admin
from django.urls import path 
from videocon import views

urlpatterns = [
    path('video/', views.index , name = 'videocon'),

]