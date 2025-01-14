from django.contrib import admin
from .models import Tag, BlogPost, Category, Author

# Register your models here.
admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Author)