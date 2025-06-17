from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import CustomUser
from myapp.models import Announcement

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = [
            'categories', 'title', 'description', 'price', 'location',
            'brand', 'model', 'production_year'
        ]
        labels = {
            'categories': 'Kategorie',
            'title': 'Tytuł',
            'description': 'Opis',
            'price': 'Cena',
            'location': 'Lokalizacja',
            'brand': 'Marka',
            'model': 'Model',
            'production_year': 'Rok produkcji',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }