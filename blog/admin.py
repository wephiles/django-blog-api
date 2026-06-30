from django.contrib import admin

from .models import Category, Article, Comment, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
