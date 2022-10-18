from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'article')
admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
