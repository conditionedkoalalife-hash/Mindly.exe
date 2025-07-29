from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def register(request):
    # Your registration logic
    return render(request, 'register.html')

def login_view(request):
    # Your login logic
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def journal_view(request):
    return render(request, 'journal.html')

def affirmations_view(request):
    return render(request, 'affirmations.html')

def connect_view(request):
    return render(request, 'connect.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Logs in the user right after registering
            return redirect('home')  # This is what's taking you to homepage
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})