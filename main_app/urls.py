from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #home route
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('logged', views.logged, name='logged')
]
=======
    path('', views.home, name='home')
]
>>>>>>> submaster
