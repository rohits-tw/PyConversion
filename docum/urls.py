from django.contrib import admin
from django.urls import path
from docum import views

urlpatterns = [
    path('',views.docx2pdf_converter, name = 'docversion'),
]