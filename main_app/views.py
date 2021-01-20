from django.core.files.base import ContentFile
from django.http.request import QueryDict
from main_app.models import Profile, Post
from main_app.forms import Profile_Form, User_Profile_Form, User_Update_Form
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


from django.core.mail import EmailMessage, send_mail

# Create your views here.

#=================================ROUTES====================================#

def home (request):
    # send_mail(
    #     'subject this',
    #     'hello future',
    #     'email@example.com',
    #     ['rcavalleir@gmail.com'],
    #     fail_silently=False
    # )
    

    # error_message= error_message
    authentication_form = AuthenticationForm()
    user_form = User_Profile_Form()
    profile_form = Profile_Form()
    context = {'user_form': user_form, 'profile_form': profile_form, 'auth_form': authentication_form }
    # context = {'user_form': user_form, 'profile_form': profile_form, 'error_message': error_message}
    return render(request, 'home.html', context)

def profile(request):
    posts = Post.objects.all()
    context = {'cities': cities, 'posts': posts}
    return render(request, 'trips/profile.html', context)


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
            send_email(user)
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

def profile_update(request):
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


def show_post(request, post_id):
    # print(post_id)
    post = Post.objects.get(id=post_id)

    context = {'post': post}
    return render(request, 'trips/show.html', context)

def post_create(request, city_id):
    form = Post_Form(request.POST)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.city_id = city_id
        new_post.save()
    return redirect('cities_detail', city_id = city_id)

def posts_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method =='POST':
        post_form = Post_Form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts_detail', post_id=post.id)

    post_form = Post_Form(instance=post)
    context = {'post_form': post_form, 'post': post}
    return render(request, 'posts/edit.html', context)

def posts_delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('cities_index')



# ========================== FUNCTIONS =============================== #


def send_email(user):
    print(user)
    email_subject = 'WELCOME TO WAYFARE!'
    email_message = f'HELLO {user.first_name}!\n\nTHANK YOU FOR CREATING A WAYFARE ACCOUNT!'
    email = EmailMessage( email_subject, email_message, to=[f'{user.email}'], reply_to=['deesoaks@mail.com '])
    email.send()



#fake db for cities seed data
class City:

    def __init__(self, id, name, description, img="#"):
        self.id = id
        self.name = name
        self.description = description
        self.img = img
        
descrip = "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi."
    
cities = [

    City("one", "Fairbanks", descrip ),
    City("two", "Big Bear", descrip ),
    City("three", "Crested Butte", descrip ),
    City("four", "New York", descrip ),
    
]
