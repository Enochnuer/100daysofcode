from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user


class BlogPost(models.Model):
    STATUS_CHOICES= (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=50)
    content = HTMLField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}" 
    
    class Meta:
        ordering= ['created_at']
       
        



