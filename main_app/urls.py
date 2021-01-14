from django.urls import path
from . import views

urlpatterns = [
    #home route
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('logged', views.logged, name='logged')
]
