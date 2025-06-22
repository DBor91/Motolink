from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import AnnouncementForm
from django.views.generic.detail import DetailView
from .models import Announcement
from django.shortcuts import get_object_or_404

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcements/announcement_detail.html'
    context_object_name = 'announcement'

def home(request):
    latest_announcements = Announcement.objects.all().order_by('-date_added')[:3]
    return render(request, "home.html", {"latest_announcements": latest_announcements})

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
    announcements = Announcement.objects.all().order_by('-date_added')  # Newest first
    return render(request, 'announcements/announcements.html', {'announcements': announcements})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.user = request.user
            announcement.save()
            form.save_m2m()
            return redirect('announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create/create_announcement.html', {'form': form})

@login_required
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    # Sprawdź uprawnienia: właściciel lub admin
    if not (request.user == announcement.user or request.user.is_superuser):
        return redirect('announcements')
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcements/edit/edit_announcement.html', {'form': form, 'announcement': announcement})