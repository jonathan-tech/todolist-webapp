
from django.urls import path, include
from .import views #imports all views files


urlpatterns = [
    #forwards to views.py, calls singup function
    path('signup',views.signup, name='signup'),
    #forwards to views.py, calls login function
    path('login',views.login, name='login'),
    #forwards to views.py, calls logout function
    path('logout',views.logout, name='logout'),
]
