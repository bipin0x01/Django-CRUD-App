from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writers_form),
    path('list/', views.writers_list)
]
