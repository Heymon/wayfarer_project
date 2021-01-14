<<<<<<< HEAD
from main_app.forms import UserProfileForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home (request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('logged')
    
    user_form = UserProfileForm()
    context = {'user_form': user_form}
    return render(request, 'registration/signup.html', context)

def logged(request):
    return render(request, 'logged.html')
=======
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, 'trips/home.html')

def about(request):
    return render(request, 'about.html')


# =============== Signup Route ================

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Username or Password'


    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'trips/signup.html', context)
>>>>>>> submaster
