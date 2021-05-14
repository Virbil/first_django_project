from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('log-in', views.log_in),
    path('new', views.register),
    path('list-users', views.list_users),
]