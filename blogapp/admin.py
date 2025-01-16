from django.contrib import admin
from .models import Tag, BlogPost, Category, Author

class TagAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_display = ('name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name')
    search_fields = ('name')

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'category', 'created_at')
    list_filter = ('status', 'category', 'tags', 'created_at')
    search_fields = ('title', 'content', 'author')










# Register your models here.
admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Author)