from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from .models import Profile, Tree, Message 


admin.site.register(Profile)
admin.site.register(Tree)
admin.site.register(Message)
