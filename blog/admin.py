from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    inlines = [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post, PostAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Comment, CommentAdmin)