from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DjUserAdmin

@admin.register(get_user_model())
class UserAdmin(DjUserAdmin):

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active"
    )

    list_filter = ("is_active",)

    ordering = ("first_name",)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )