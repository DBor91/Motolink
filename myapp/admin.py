from django.contrib import admin
from .models import CustomUser, Category, Announcement, AnnouncementCategory

admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Announcement)
admin.site.register(AnnouncementCategory)