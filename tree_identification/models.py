from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings


# MODELS FOR THE USER AUTHENTICATION
# Model to store Contact form data
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"


# Model to store Registration form data
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def get_image_url(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        else:
            return os.path.join(settings.MEDIA_URL, "profile_pics/default.png")


# Model to get the user for password confirmation
class PasswordResetConfirmView(models.Model):
    uidb64 = models.CharField(max_length=100)
    token = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.uidb64}"


# MODELS FOR THE TREE IDENTIFICATION
# Model to represent the tree data
class Tree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    common_name = models.CharField(max_length=200, null=True, blank=True)
    tree_type = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    introduction = models.TextField(max_length=800, null=True, blank=True)
    tree_image = models.ImageField(upload_to="tree_images/")
    tree_habitat = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.common_name

    # Model to save messages to the user from the admin


class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
