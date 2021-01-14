from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    #home route
    path('', views.home, name='home'),

    path('about/', views.about),

    path('accounts/signup', views.signup, name='signup'),
]
=======
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]

>>>>>>> master
