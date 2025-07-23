from django.contrib import admin
from .models import Blog, Category, Tag, Comment
# Register your models here.
# admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'is_slider', 'is_featured']
    prepopulated_fields = {'slug': ('title')}
    list_editable = ['is_slider', 'is_featured']
    search_fields = ['title', 'category']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)