from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.model):
    name = models.CharField(max_length=50, unique=True)

class Tag(models.model):
    name = models.CharField(max_length=50, unique=True)

class Author(models.model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

class BlogPost(models.model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL
        null=True,
        blank=True
    )



