from django.urls import path
from . import views
from .views import register
from .views import announcements
from .views import create_announcement

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', register, name='register'),
    path('announcements/', announcements, name='announcements'),
    path('announcements/create', create_announcement, name='create_announcement'),
    path('announcements/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('announcements/<int:pk>/edit/', views.edit_announcement, name='edit_announcement')
]