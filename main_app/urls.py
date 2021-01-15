from django.urls import path
from . import views

urlpatterns = [
    #home route
    path('', views.home, name='home'),

<<<<<<< HEAD
    path('accounts/signup', views.signup, name='signup'),
    
    path('', views.profile, name='profile')
=======
    path('about/', views.about),

    path('accounts/signup', views.signup, name='signup'),
]
=======
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile')
>>>>>>> f9c57f6c4876e5f36d8b3babf921e358cd0bce32
]

