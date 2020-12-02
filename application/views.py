from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import Image, Profile
from django import forms


def home(request):
    images = Image.get_all_images()
    
    return render(request, 'index.html', {'images':images})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def plans(request):
    one = '100'
    two = '250'
    three = '500'
    four = '1,000'
    five = '5,000'
    six = '10,000'
    return render(request, 'plans.html',{'one':one, 'two':two, 'three':three, 'four':four, 'five':five, 'six':six})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile
            return render(request,'registration/login.html')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    return redirect('signup')

def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Tujengane photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})

