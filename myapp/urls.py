from django.urls import path
from . import views
from .views import register
from .views import announcements

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', register, name='register'),
    path('announcements/', announcements, name='announcements')
]