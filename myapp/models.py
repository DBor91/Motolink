from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self): return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    production_year = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)


    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='announcements'
    )

    categories = models.ManyToManyField(
        Category,
        through='AnnouncementCategory',
        related_name='announcements'
    )

    def __str__(self): return self.title


class AnnouncementCategory(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['announcement', 'category']]