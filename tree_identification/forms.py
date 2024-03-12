from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from .models import Message, Tree


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already taken.")
        return email


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    current_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Profile
        fields = ["image", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = self.instance.user
        if User.objects.filter(email=email).exclude(username=user.username).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")
        current_password = cleaned_data.get("current_password")

        # Check if the current password is correct
        if not self.instance.user.check_password(current_password):
            raise forms.ValidationError("The current password is incorrect.")

        # Validate new password and its confirmation
        if new_password and new_password != confirm_new_password:
            raise forms.ValidationError("The new passwords do not match.")

        return cleaned_data


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = [
            "common_name",
            "tree_type",
            "origin",
            "introduction",
            "tree_image",
            "tree_habitat",
        ]


# Create a form for the contact page
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
        }

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
            self.fields["name"].widget.attrs.update({"class": "form-control"})
            self.fields["email"].widget.attrs.update({"class": "form-control"})
            self.fields["subject"].widget.attrs.update({"class": "form-control"})
            self.fields["message"].widget.attrs.update({"class": "form-control"})
            for field in self.fields:
                self.fields[field].widget.attrs["class"] = "form-control"
                self.fields[field].widget.attrs["placeholder"] = self.fields[
                    field
                ].label
                self.fields[field].label = False
                self.fields[field].help_text = ""
                self.fields[field].required = True
