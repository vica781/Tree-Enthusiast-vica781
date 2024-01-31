from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # add `email` field to the form
    # because it is not included in the default UserCreationForm
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    # fields that will be shown are username, email, password1, password2
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


# Create a form for updating the user profile
class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Profile
        fields = ["image"]

    def clean(self):
        # Add validation for passwords
        cleaned_data = super().clean()
        return cleaned_data
