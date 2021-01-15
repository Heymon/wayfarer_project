from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Profile(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)
    cur_country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} is currently living in {self.cur_country}"