from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from .models import Profile

admin.site.register(Profile)
