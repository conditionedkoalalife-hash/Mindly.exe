from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Home view
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # force login before accessing home
    return render(request, 'home.html')

# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created! Please log in.')
        return redirect('login')
    
    return render(request, 'register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render

def journal_view(request):
    saved_entry = request.session.get('journal_entry', '')
    message = ''

    if request.method == 'POST':
        entry = request.POST.get('entry')
        request.session['journal_entry'] = entry
        saved_entry = entry
        message = "Journal entry saved ✅"

    return render(request, 'journal.html', {
        'saved_entry': saved_entry,
        'message': message
    })
