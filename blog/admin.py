# from django.contrib import admin
# from .models import Blog, Category, Tag, Comment
# # Register your models here.
# # admin.site.register(Blog)
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug', 'category', 'is_slider', 'is_featured']
#     prepopulated_fields = {'slug': ('title',)}
#     list_editable = ['is_slider', 'is_featured']
#     search_fields = ['title', 'category']

# admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Comment)

from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display= ['title', 'slug', 'category', 'is_slider', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_slider', 'is_featured']
    search_fields = ['title', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name']
    prepopulated_fields={'slug':("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['user','email','comment','blog']
    search_fields=['user','email','comment']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=['id','name']
    search_fields=['name']


