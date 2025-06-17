from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm


# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user to the database
            login(request, user)  # Optionally log the user in after registration
            return redirect('home')  # Redirect to homepage or another page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def announcements(request):
    return render(request, 'announcements/announcements.html')

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user
            announcement.save()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create/create_announcement.html', {'form': form})