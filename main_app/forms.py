from main_app.models import Profile
from django.forms import ModelForm, fields



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, Post
from django import forms

class User_Profile_Form(UserCreationForm):
    email = forms.EmailField(label= "Email")
    first_name = forms.CharField(label= "First Name")
    last_name = forms.CharField(label= "Last Name")
    # cur_country = forms.CharField(label= "Current Country")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(User_Profile_Form, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        # user.objects.profile_set.all()[0].cur_country = self.cleaned_data["cur_country"]
        if commit:
            user.save()
        return user

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        labels = {'cur_city': 'Current City'}
        fields = ['cur_city',]

# class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
#     def confirm_login_allowed(self, user):
#         pass
        
class User_Update_Form(ModelForm):
    first_name = forms.CharField(label= "First Name")
    last_name = forms.CharField(label= "Last Name")

    class Meta:
        model = User
        fields = ("first_name", "last_name")


class Post_Form(ModelForm):
    class Meta:
        model = Post
        # labels = {'title': 'Title', 'location': 'Location'}
        fields = ['title', 'text', 'location']