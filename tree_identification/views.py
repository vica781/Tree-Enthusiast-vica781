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
from .models import Profile, Message
from .forms import ProfileUpdateForm, UserRegisterForm, MessageForm
from django.contrib.auth import get_user_model, update_session_auth_hash
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
        "page_title": "Home",
        "content": "Welcome to the home page!",
        "date_posted": datetime.now(),
        "current_year": datetime.now().year,
    }
    return render(request, "home.html", context)


def browse_trees(request):
    trees = Tree.objects.all()
    context = {"page_title": "Browse Trees", "trees": trees}
    return render(request, "browse_trees.html", context)


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}!")
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
    return render(
        request,
        "register.html",
        context={
            "page_title": "Sign Up",
        },
    )


def check_username(request):
    username = request.GET.get("username", None)
    response = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(response)


def check_email(request):
    email = request.GET.get("email", None)
    response = {
        "is_taken": User.objects.filter(email__iexact=email).exists()
        and request.user.email != email
    }
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
    return render(request, "login.html", context={"page_title": "Login"})


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
        Message.objects.create(name=name, email=email, subject=subject, message=message)

        # Send confirmation email
        send_mail(
            "Confirmation - We Received Your Message",
            "Thank you for contacting us. We have received your message and will respond shortly.",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")

    return render(
        request,
        "contact.html",
        context={
            "page_title": "Sign Up",
        },
    )

@login_required
def profile_user(request):
    return render(request, "profile.html", context={"page_title": "Your Profile"})


from django.contrib.auth import update_session_auth_hash


@login_required
def profile_update(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=profile, initial={"email": user.email}
        )

        # Get the 'current_password' from the form
        current_password = request.POST.get("current_password")

        # Now manually check if the current password is correct
        if not user.check_password(current_password):
            # If the password is incorrect, add a custom error message
            messages.error(request, "The current password you entered is incorrect.")
            return render(request, "profile_update.html", {"form": form})

        if form.is_valid():
            # Handle Email Update
            new_email = form.cleaned_data.get("email")
            if new_email and new_email != user.email:
                user.email = new_email
                user.save()

            # Handle Password Update
            new_password = form.cleaned_data.get("new_password")
            if new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(
                    request, user
                )  # Prevents user from being logged out.

            # Save profile (for image and other profile-related updates)
            form.save()

            messages.success(request, "Your profile has been updated successfully.")
            return redirect("profile")
        else:
            # If form is not valid, render the form with errors
            return render(request, "profile_update.html", {"form": form})
    else:
        form = ProfileUpdateForm(instance=profile, initial={"email": user.email})

    return render(request, "profile_update.html", {"form": form})


@login_required
def profile_delete(request, user_id):
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

    return render(
        request, "add_tree.html", context={"page_title": "Add Tree", "form": form}
    )


@login_required
def my_trees(request):
    trees = Tree.objects.filter(user=request.user)  # Fetch trees for the logged-in user
    return render(
        request, "my_trees.html", context={"page_title": "My Trees", "trees": trees}
    )


def tree_detail(request, tree_id):
    tree = get_object_or_404(Tree, id=tree_id)
    return render(
        request,
        "tree_detail.html",
        context={"page_title": "Tree Details", "tree": tree},
    )


@login_required
def edit_tree(request, tree_id):
    tree = get_object_or_404(Tree, id=tree_id, user=request.user)
    if request.method == "POST":
        form = TreeForm(request.POST, request.FILES, instance=tree)
        if form.is_valid():
            form.save()
            messages.success(request, "Tree information updated successfully!")
            return redirect("my_trees")
        else:
            messages.error(request, "Error updating tree information.")
    else:
        form = TreeForm(instance=tree)
    return render(
        request, "edit_tree.html", context={"page_title": "Edit Tree", "form": form}
    )


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
    return render(
        request, "identification_guide.html", context={"page_title": "Trees' Guide"}
    )


def search_trees(request):
    query = request.GET.get("q")
    if query:
        trees = Tree.objects.filter(common_name__icontains=query)
    else:
        trees = Tree.objects.none()
    return render(
        request,
        "search_results.html",
        context={"page_title": "Search Results", "trees": trees},
    )


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # Create a new Message instance and save it to the database
            Message.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                subject=form.cleaned_data.get(
                    "subject", ""
                ),  # 'subject' might be optional
                message=form.cleaned_data["message"],
            )
            return redirect("contact_success")
    else:
        form = MessageForm()

    return render(
        request, "contact.html", context={"page_title": "Contact", "form": form}
    )


def contact_success(request):
    return render(request, "contact_success.html", {})
