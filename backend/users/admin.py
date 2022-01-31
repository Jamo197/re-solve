from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)