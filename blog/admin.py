from django.contrib import admin

from .models import Category, Post, Project, About

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(About)
