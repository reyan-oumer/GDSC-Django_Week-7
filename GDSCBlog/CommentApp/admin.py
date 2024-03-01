from django.contrib import admin

# Register your models here.
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'published_date', 'post')

admin.site.register(Comment,CommentAdmin)