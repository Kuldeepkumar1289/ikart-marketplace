from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Roles & Profile', {'fields': ('is_customer', 'is_vendor', 'phone_number')}),
    )
    list_display = ('username', 'email', 'is_customer', 'is_vendor', 'is_staff')