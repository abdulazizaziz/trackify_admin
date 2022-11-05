from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User

# Register your models here.


class AccountAdmin(BaseUserAdmin):
    fieldsets = [
        (
            "Personal Info",
            {
                "fields": [
                    "email",
                    "password",
                    "name",
                    "groups",
                    "is_superuser",
                    "is_active",
                    "is_staff",
                ]
            },
        ),
        ("User Permission", {"fields": ["user_permissions"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "fields": [
                    "email",
                    "name",
                    "password1",
                    "password2",
                ]
            },
        )
    ]
    list_display = ["name", "email"]
    ordering = ["name"]


# admin.site.unregister(User)
admin.site.register(User, AccountAdmin)
