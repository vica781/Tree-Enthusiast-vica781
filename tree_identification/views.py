from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import ProfileUpdateForm
from .models import Profile


def home(request):
    context = {
        "title": "Home Page",
        "content": "Welcome to the home page!",
        "date_posted": datetime.now(),
    }
    return render(request, "home.html", context)


def register_user(request):
    # if the request is a POST request, then the user is trying to register
    if request.method == "POST":
        # create a form with the POST data
        form = UserRegisterForm(request.POST)
        print(form)
        # check if the form is valid
        if form.is_valid():
            # save the user to the database
            form.save()
            # get the username
            username = form.cleaned_data.get("username")
            # TODO: GET THE PASSWORD
            # Get the password
            password = form.cleaned_data.get("password1")
            # Authenticate the user

            user = authenticate(username=username, password=password)
            # Log the user in
            login(request, user)

            # TODO: AUTHENTICATE THE USER

            # TODO: LOG THE USER IN
            # display a success message
            messages.success(request, f"Account created for {username}!")
            # redirect to the home page
            return redirect("home")
        else:
            # Log form errors for debugging
            print("Form errors:", form.errors)
            messages.error(request, "Invalid data!")
    else:
        # if the request is not a POST request,
        # then the user is trying to access the registration page
        # create an empty form
        form = UserRegisterForm()
    # render the registration page
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        # get the username and password from the POST data
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        # authenticate the user
        user = authenticate(request, username=username, password=password)
        # if the user is authenticated
        if user is not None:
            # log the user in
            login(request, user)
            print("User logged in")
            # redirect to the home page
            messages.success(request, f"Logged in as {username}!")
            return redirect("home")
        else:
            # display an error message
            messages.error(request, "Invalid username or password!")
            # redirect to the login page
            return redirect("login")
    # render the login page
    return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message")

        # Save the message in the database
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # Send confirmation email
        send_mail(
            "Confirmation - We Received Your Message",
            "Thank you for contacting us. We have received your message and will respond shortly.",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")

    return render(request, "contact.html", {})


def profile_user(request):
    return render(request, "profile.html", {})


def profile_update(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect("profile")  # Redirect to the profile view
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "profile_update.html", {"form": form})
