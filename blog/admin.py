from django.contrib import admin
from .models import  BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'read']
    readonly_fields = ['read', ]
    ordering = ['-date', ]
    search_fields = ['title','content']

admin.site.register(BlogPost, BlogPostAdmin)