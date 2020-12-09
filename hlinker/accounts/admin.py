from .models import User
from django.contrib.auth.admin import UserAdmin as InheritableUserAdmin
from django.contrib import admin


class UserAdmin(InheritableUserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
