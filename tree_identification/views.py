from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def register(request):
    # if the request is a POST request, then the user is trying to register
    if request.method == 'POST':
        # create a form with the POST data
        form = UserRegisterForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            # save the user to the database
            form.save()
            # get the username
            username = form.cleaned_data.get('username')
            # display a success message
            messages.success(request, f'Account created for {username}!')
            # redirect to the home page
            return redirect('tree_identification-home')
    else:
        # if the request is not a POST request, 
        # then the user is trying to access the registration page
        # create an empty form
        form = UserRegisterForm()
    # render the registration page
    return render(request, 'tree_identification/register.html', {'form': form})


