from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp.models import CustomUser
from myapp.models import Announcement, Category

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class AnnouncementForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Kategorie"

    )

    def clean_production_year(self):
        year = self.cleaned_data.get('production_year')
        if not (1000 <= int(year) <= 9999):
            raise forms.ValidationError("Rok produkcji musi mieć dokładnie 4 cyfry.")
        if int(year) < 1930 or int(year) > 2025:
            raise forms.ValidationError("Rok produkcji musi być w zakresie 1930-2025.")
        return year

    class Meta:
        model = Announcement
        fields = [
            'categories', 'title', 'description', 'price', 'location',
            'brand', 'model', 'production_year'
        ]
        labels = {
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
            'production_year': forms.NumberInput(attrs={
                'min': 1930,
                'max': 2025,
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'min': 1,
            }),


        }

