from django.db import models
from django.contrib.auth.models import User


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


# Model to store Login form data
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.username}"


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
    # common_name = models.CharField(max_length=200)
    # type = models.CharField(max_length=200)
    # origin = models.CharField(max_length=200)
    # introduction = models.TextField()
    # tree_image = models.ImageField(upload_to="tree_images/")
    # tree_image2 = models.ImageField(upload_to="tree_images/", blank=True)
    # tree_image3 = models.ImageField(upload_to="tree_images/", blank=True)
    # tree_habitat = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="tree_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
