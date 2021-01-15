from django.http.request import QueryDict
from main_app.models import Profile
from main_app.forms import Profile_Form, UserProfileForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home (request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')


def about (request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        mutable_POST = request.POST.copy()
        user_country = QueryDict(f'cur_city={mutable_POST.pop("cur_city")[0]}')

        print(request.POST["username"])
        user_form = UserProfileForm(mutable_POST)
        if user_form.is_valid():
            user = user_form.save()
            #creates profile/connects to user
            profile = Profile_Form(user_country)
            user_profile = profile.save(commit=False)
            user_profile.user = user
            user_profile.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = user_form.errors
            print(error_message)
            # return redirect('signup', error_message)
    
    # error_message = 
    user_form = UserProfileForm()
    profile_form = Profile_Form()
    context = {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

