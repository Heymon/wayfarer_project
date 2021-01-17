from django.http.request import QueryDict
from main_app.models import Profile
from main_app.forms import Profile_Form, User_Profile_Form, User_Update_Form
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def home (request):
    # error_message= error_message
    authentication_form = AuthenticationForm()
    user_form = User_Profile_Form()
    profile_form = Profile_Form()
    context = {'user_form': user_form, 'profile_form': profile_form, 'auth_form': authentication_form }
    # context = {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'trips/profile.html')


def about (request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        mutable_POST = request.POST.copy()
        user_country = QueryDict(f'cur_city={mutable_POST.pop("cur_city")[0]}')

        print(request.POST["username"])
        user_form = User_Profile_Form(mutable_POST)
        if user_form.is_valid():
            user = user_form.save()
            #creates profile/connects to user
            profile = Profile_Form(user_country)
            user_profile = profile.save(commit=False)
            user_profile.user = user
            user_profile.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = user_form.errors
            print(error_message)
            # return redirect('home', error_message)
            return redirect('home')
    
    # error_message = 
    # user_form = UserProfileForm()
    # profile_form = Profile_Form()
    # context = {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message}
    # return render(request, 'registration/signup.html', context)

def update(request):
    print('isnotvalid')
    user = request.user
    if request.method =='POST':
        print('isnotvalid')
        mutable_POST = request.POST.copy()
        user_country = QueryDict(f'cur_city={mutable_POST.pop("cur_city")[0]}')
        user_update_form = User_Update_Form(mutable_POST, instance=user)
        profile_form = Profile_Form(user_country, instance=user.profile)
        print('isnotvalid')
        if user_update_form.is_valid():
            user_update_form.save()
            profile_form.save()
            print('isvalid') 

    user_update_form = User_Update_Form(instance=user)
    profile_form = Profile_Form(instance=user.profile)
    context = {'profile_form': profile_form, 'user_update_form': user_update_form}
    return render(request, 'trips/update.html', context)