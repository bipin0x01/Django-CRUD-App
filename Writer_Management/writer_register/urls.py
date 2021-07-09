from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.writers_form,name='writers_insert'), #get and post req for insert operations
    path('list/', views.writers_list,name='writers_list'), #get and post req to retrieve and populate list table.
    path('<int:id>/',views.writers_form,name='writers_update'), #get and post req for update operations
    path('delete/<int:id>/',views.writers_delete,name='writers_delete') #get and post req for delete operations
]
