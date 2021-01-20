from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.

class Profile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    profile_img = models.URLField(max_length=100, default="https://picsum.photos/200")
    cur_city = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.user.username} is currently living in {self.cur_city}"

class City(models.Models):
    name = models.CharField(maxlength=100)
    image = models.URLField(maxlength=200)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    # img = models.URLField(max_length=100)
    location = ForeignKey(City, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    user = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    last_edit = DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post from {self.user.username} in {self.location} created in {self.created_at.date()} edited in {self.last_edit.strftime('%a %b %d %H:%M %Z')}"



