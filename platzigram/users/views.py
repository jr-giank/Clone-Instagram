#Importaciones de Django
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError

#Modelos 
from django.contrib.auth.models import User
from users.models import Profile

#Importaciones de formularios de usuarios
from users.forms import ProfileForm, SignUpForm

# Create your views here.
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Username or Password incorret'})
    
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)

    return redirect('login')

def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form':form})

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.profile_picture = data['profile_picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )