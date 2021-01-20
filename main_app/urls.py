from django.urls import path
from . import views

urlpatterns = [
    #home route
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.update, name='update'),
    #path('cities/', views.cities_index, name='cities_index'),
    #path('cities/<int:city_id>/', views.cities_detail, name='cities_detail'),
    path('cities/<int:city_id>/post/post_create', views.post_create, name='post_create'),
    path('post/<int:post_id>', views.show_post, name='show_post'),
    path('posts/<int:post_id>/edit', views.posts_edit, name='posts_edit'),
    path('posts/<int:post_id>/delete', views.posts_delete, name='posts_delete'),
    path('accounts/signup', views.signup, name='signup'),
    
]

