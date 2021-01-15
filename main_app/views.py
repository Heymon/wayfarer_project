from main_app.forms import UserProfileForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home (request):
    return render(request, 'home.html')
    
def profile(request):
    return render(request, 'profile.html')

<<<<<<< HEAD
=======

def about (request):
    return render(request, 'about.html')
>>>>>>> f9c57f6c4876e5f36d8b3babf921e358cd0bce32

def signup(request):

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('home')
    
    user_form = UserProfileForm()
    context = {'user_form': user_form}
    return render(request, 'registration/signup.html', context)

