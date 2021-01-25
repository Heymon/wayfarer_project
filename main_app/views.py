from django.core.files.base import ContentFile
from django.http.request import QueryDict
from django.http.response import HttpResponse

from django.shortcuts import render, redirect

# =============MODELS & FORMS===============
from main_app.models import Profile, Post, City
from main_app.forms import Profile_Form, User_Profile_Form, User_Update_Form, Post_Form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

# =============EMAIL===============
from django.core.mail import EmailMessage, send_mail

# ===========DATE AND TIME===============
from django.utils.timezone import localtime, now
# from tzlocal import get_localzone
from datetime import datetime, timezone
# import pytz

# Create your views here.

#=================================ROUTES====================================#
import json

def home (request):
    # for key, value in request.session.items():
    #     print('{} => {}'.format(key, value))
    authentication_form = None
    user_form = None
    profile_form = None
    
    if 'signup_error' in request.session:
        user_form = User_Profile_Form(request.session['signup_error'])
        profile_form = Profile_Form(request.session['cur_profile'])
        # print(user_form)
        del request.session['signup_error']
        del request.session['cur_profile']
    else:
        user_form = User_Profile_Form()
        profile_form = Profile_Form()

    if 'login_error' in request.session:
        # print(request.session['login_error'])
        authentication_form = AuthenticationForm(data=request.session['login_error'])
        # print(authentication_form)
        del request.session['login_error']
    else:
        authentication_form = AuthenticationForm()
   
    context = {'user_form': user_form, 'profile_form': profile_form, 'auth_form': authentication_form }
    # context = {'user_form': user_form, 'profile_form': profile_form, 'auth_form': authentication_form, 'signup_error': signup_error_message}
    return render(request, 'home.html', context)


def profile(request):
    
    post_form = Post_Form
    posts = request.user.post_set.all().order_by('-created_at')
    cities = City.objects.all()
    # print(get_localzone())
    # print(request.user.date_joined.astimezone(tz=pytz.timezone('US/Pacific')).date())
    print((localtime(now()).date()-request.user.date_joined.date()).days)
    print(request.user.date_joined.date().day)
    context = {'cities': cities, 'posts': posts, 'post_form': post_form, 'cur_date': localtime(now()).date()}
    return render(request, 'trips/profile.html', context)


def about (request):

    authentication_form = AuthenticationForm()
    user_form = User_Profile_Form()
    profile_form = Profile_Form()
   
    context = {'user_form': user_form, 'profile_form': profile_form, 'auth_form': authentication_form }
    return render(request, 'about.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        mutable_POST = request.POST.copy()
        user_country = QueryDict(f'cur_city={mutable_POST.pop("cur_city")[0]}')

        # print(request.POST["username"])
        user_form = User_Profile_Form(mutable_POST)
        if user_form.is_valid():
            user = user_form.save()
            #creates profile/connects to user
            profile = Profile_Form(user_country)
            user_profile = profile.save(commit=False)
            user_profile.user = user
            user_profile.save()
            send_email(user)
            login(request, user)
            return redirect('profile')
        else:
            request.session['cur_profile'] = user_country
            request.session['signup_error'] = mutable_POST
            return redirect('home')


def custom_login(request):

    authentication_form = AuthenticationForm(data=request.POST)
    # print(authentication_form['username'])
    # print(request.POST['username'])
    
    if authentication_form.is_valid():
        print('valid')
        # username = request.POST['username']
        # password = request.POST['password']
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('profile')
    else:
        print('not valid')
        # print(authentication_form)
        request.session['login_error'] = request.POST
        return redirect('home')
    

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
            return redirect('profile')

    user_update_form = User_Update_Form(instance=user)
    profile_form = Profile_Form(instance=user.profile)
    context = {'profile_form': profile_form, 'user_update_form': user_update_form}
    return render(request, 'trips/update.html', context)

def cities_detail(request, city_id):
    post_form = Post_Form
    cities = City.objects.all()
    city_page = City.objects.get(id=city_id)
    # print(cities.get(id='1').name)
    posts = City.objects.get(id=city_id).post_set.all().order_by('-created_at')
    # print(request)

    # context = {'cities': cities, 'posts': posts, 'city_id': city_id, 'post_form': post_form}
    context = {'cities': cities, 'posts': posts, 'city_page': city_page, 'post_form': post_form}
    return render(request, 'trips/cities.html', context)  

def show_post(request, post_id):
    # print(post_id)
    post = Post.objects.get(id=post_id)
    post_form = Post_Form(instance=post)

    context = {'post': post, 'post_form': post_form}
    return render(request, 'posts/show.html', context)

def post_create(request):
    form = None
    direction = ''
    if 'redirect' in request.POST:
        mutable_POST = request.POST.copy()
        print(mutable_POST)
        # print(QueryDict(f'route={mutable_POST.pop("redirect")[0]}'))
        direction = mutable_POST.pop("redirect")[0]
        print(direction)
        form = Post_Form(mutable_POST)
    else:
        form = Post_Form(request.POST)

    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.user = request.user
        # new_post.city_id = city_id
        new_post.save()

    if direction:
        return redirect('cities_detail', direction)
    return redirect('profile')

def posts_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method =='POST':
        post_form = Post_Form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_post', post_id=post.id)

    post_form = Post_Form(instance=post)
    context = {'post_form': post_form, 'post': post}
    return render(request, 'posts/edit.html', context)

def posts_delete(request, post_id):
    
    Post.objects.get(id=post_id).delete()
    return redirect('cities_detail', city_id = 1)



# ========================== FUNCTIONS =============================== #


def send_email(user):
    print(user)
    email_subject = 'WELCOME TO WAYFARE!'
    email_message = f'HELLO {user.first_name}!\n\nTHANK YOU FOR CREATING A WAYFARE ACCOUNT!'
    email = EmailMessage( email_subject, email_message, to=[f'{user.email}'], reply_to=['deesoaks@mail.com '])
    email.send()



#fake db for cities seed data
# class City:

#     def __init__(self, id, name, description, img="#"):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.img = img
        
# descrip = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi."
    
# cities = [

#     City("zero", "Aspen", descrip ),
#     City("one", "Fairbanks", descrip ),
#     City("two", "Big Bear", descrip ),
#     City("three", "Crested Butte", descrip ),
#     City("four", "New York", descrip ),
    
# ]
