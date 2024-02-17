from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model,
)  # authenticate is used to check if the user is valid
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact, Profile
from .forms import ProfileUpdateForm, UserRegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Tree
from .forms import TreeForm
from django.shortcuts import get_object_or_404
import logging


# from django.contrib.auth import get_user_model
User = get_user_model()


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
            # Get the password
            password = form.cleaned_data.get("password1")
            # Authenticate the user
            user = authenticate(username=username, password=password)
            # Log the user in
            login(request, user)
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


def check_username(request):
    username = request.GET.get("username", None)
    response = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(response)


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


@login_required
def profile_update(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)

        # Check if the form is valid
        if form.is_valid():
            # Check the current password if it's provided
            current_password = form.cleaned_data.get("current_password")
            if not user.check_password(current_password):
                messages.error(request, "The current password is incorrect.")
                return render(
                    request, "profile_update.html", {"form": form}
                )  # Re-render the page with the form

            # Check if there are changes in the form
            if form.has_changed():
                # Perform the update
                form.save()
                messages.success(request, "Your profile has been updated successfully.")
            else:
                # No changes were made
                messages.info(request, "No changes were detected in your profile.")
            return redirect("profile")  # Redirect to the profile view
        else:
            # Form is not valid
            messages.error(request, "Please correct the error below.")
    else:
        form = ProfileUpdateForm(instance=user.profile)

    return render(request, "profile_update.html", {"form": form})


@login_required
def profile_delete(request):
    if request.method == "POST":
        # Retrieve the password from the form
        password = request.POST.get("confirm_password")

        # Debugging: Print the password and username to the console (remove in production)
        print(f"Password received: {password}")
        print(f"User: {request.user.username}")

        # Manually check the password
        if request.user.check_password(password):
            username = request.user.username  # Store the username before deletion
            request.user.delete()  # Delete the user
            messages.info(
                request, f"{username}'s profile has been successfully deleted!"
            )
            return redirect("home")
        else:
            # If password check fails, inform the user
            messages.error(request, "Password is incorrect. Profile was not deleted.")
            return redirect("profile")


@login_required
def add_tree(request):
    logger = logging.getLogger(__name__)
    logger.debug("Add tree view called")
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            tree = form.save(commit=False)
            tree.user = request.user
            tree.save()
            logger.debug(f"Tree saved: {tree}")
            messages.success(request, "Tree added successfully!")
            return redirect("home")
        else:
            logger.warning(f"Form invalid: {form.errors}")
            # Consider adding a message here for form invalidity
            messages.error(request, "There was an error with your submission.")
    else:
        form = TreeForm()

    return render(request, "add_tree.html", {"form": form})


@login_required
def my_trees(request):
    trees = Tree.objects.filter(user=request.user)  # Fetch trees for the logged-in user
    return render(request, "my_trees.html", {"trees": trees})


@login_required
def tree_detail(request, tree_id):
    tree = get_object_or_404(
        Tree, id=tree_id, user=request.user
    )  # Ensure the tree belongs to the logged-in user
    return render(request, "tree_detail.html", {"tree": tree})


@login_required
def edit_tree(request, tree_id):
    tree = get_object_or_404(Tree, id=tree_id, user=request.user)
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            return redirect("my_trees")
    else:
        form = TreeForm(instance=tree)
    return render(request, "edit_tree.html", {"form": form})


@login_required
def delete_tree(request, tree_id):
    tree = get_object_or_404(Tree, id=tree_id, user=request.user)
    if request.method == "POST":
        password = request.POST.get("confirm_password")

        # Authenticate the user with the provided password
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            # Password is correct, proceed with tree deletion
            tree.delete()
            messages.success(request, "Tree deleted successfully!")
            return redirect("my_trees")  # Redirect user to their trees
        else:
            # Password is incorrect
            messages.error(request, "Password is incorrect. Tree was not deleted.")
            return redirect("tree_detail", tree_id=tree_id)

    return render(request, "confirm_delete.html", {"tree": tree})


def identification_guide(request):
    return render(request, "identification_guide.html", {})
