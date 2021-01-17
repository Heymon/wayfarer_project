from django.urls import path
from . import views

urlpatterns = [
    #home route
    path('', views.home, name='home'),

    path('accounts/signup', views.signup, name='signup'),
    
    path('profile/', views.profile, name='profile'),
    path('profile/post/<int:post_id>', views.show_post, name='show_post'),
    path('profile/update', views.update, name='update'),

    path('about/', views.about, name='about'),
]

