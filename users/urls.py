# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
   path('criar', views.register_request, name='cadastrar'),
   path("login", views.login_request, name="login"),
   path("logout", views.logout_request, name= "logout"),
]
