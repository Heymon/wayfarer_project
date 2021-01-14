from django.forms import ModelForm, fields



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserProfileForm(UserCreationForm):
    email = forms.EmailField(label= "Email")
    first_name = forms.CharField(label= "First Name")
    last_name = forms.CharField(label= "Last Name")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.first_name =self.cleaned_data["first_name"]
        user.last_name =self.cleaned_data["last_name"]
        user.email =self.cleaned_data["email"]
        # user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user