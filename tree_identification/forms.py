from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    # add `email` field to the form 
    # because it is not included in the default UserCreationForm
    email = forms.EmailField()

    
    # fields that will be shown are username, email, password1, password2
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']