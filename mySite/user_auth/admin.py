# user_auth/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'date_joined', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
