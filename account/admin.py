from django.contrib import admin

from . models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['email',]
    list_display = ['email', 'name', 'is_active']

    fieldsets = (
        (None, {
            "fields": (
                ['email', 'password']
            ),
            
        }),
        ("Personal Info", {
            "fields": (
                ['name', 'birthplace', 'birth', 'phone', 'img_user']
            ),
            
        }),
        ("Permissions", {
            "fields": (
                ['groups', 'is_active', 'is_staff', 'is_admin', 'is_superuser']
            ),
            
        }),
    )

    add_fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email', 'phone', 'password1', 'password2' ]
            }
        
    )]

admin.site.register(User, UserAdmin)