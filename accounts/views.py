from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

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






# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
#
#
# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'




# Create your views here.
