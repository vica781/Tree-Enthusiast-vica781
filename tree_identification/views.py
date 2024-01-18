from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.


def home(request):
    context = {
        "title": "Home Page",
        "content": "Welcome to the home page!",
        "date_posted": datetime.now(),
    }
    return render(request, "home.html", context)


def register(request):
    # if the request is a POST request, then the user is trying to register
    if request.method == "POST":
        # create a form with the POST data
        form = UserRegisterForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save the user to the database
            form.save()
            # get the username
            username = form.cleaned_data.get("username")
            # display a success message
            messages.success(request, f"Account created for {username}!")
            # redirect to the home page
            return redirect("tree_identification-home")
    else:
        # if the request is not a POST request,
        # then the user is trying to access the registration page
        # create an empty form
        form = UserRegisterForm()
    # render the registration page
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        # get the username and password from the POST data
        username = request.POST.get("username")
        password = request.POST.get("password")
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        # if the user is authenticated
        if user is not None:
            # log the user in
            login(request, user)
            # redirect to the home page
            return redirect("tree_identification-home")
        else:
            # display an error message
            messages.error(request, "Invalid username or password!")
    # render the login page
    return render(request, "login.html")
