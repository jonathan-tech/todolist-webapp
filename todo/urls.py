
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
        #forwards to views.py, calls home function
        path('',views.home, name='home'),
        #forwards to views.py, calls create function
        path('create',views.create, name='create'),
        #forwards to views.py, calls delete function
        path('delete/<list_id>', views.delete, name='delete'),
        #forwards to views.py, calls cross_off function
        path('cross_off/<list_id>', views.cross_off, name='cross_off'),
        #forwards to views.py, calls uncross function
        path('uncross/<list_id>', views.uncross, name='uncross'),
        #forwards to views.py, calls edit function
        path('edit/<list_id>', views.edit, name='edit'),
    ]
