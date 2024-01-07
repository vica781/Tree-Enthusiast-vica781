from django.urls import path
from . import views
# from tree_identification.forms import UserRegisterForm
# from tree_identification.models import User
# from tree_identification.admin import UserAdmin
# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.db import models


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('', views.home, name='tree_identification-home'),
]