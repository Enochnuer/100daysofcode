from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture =models.ImageField(upload_to='profile_pictures', blank=True, null=True)

# Create your models here.
    def __str__(self):
        return self.username
