from django.http.request import QueryDict
from main_app.models import Profile
from main_app.forms import Profile_Form, UserProfileForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home (request):
    return render(request, 'home.html')

def signup(request):
    error = ''
    if request.method == 'POST':
        mutable_POST = request.POST.copy()
        user_country = QueryDict(f'cur_country={mutable_POST.pop("cur_country")[0]}')

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
            error = user_form.errors
            print(error)
    
    user_form = UserProfileForm()
    profile_form = Profile_Form()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'registration/signup.html', context)

