from django.contrib import admin
from django.contrib.admin import register
from .models import Post, Profile, Like
from authentication.models import CustomUser


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'image',)


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', "id", 'title', 'created_time')


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', "id", 'post')


@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')


