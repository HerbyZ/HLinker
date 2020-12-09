from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Link


class UserModelAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class LinkModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent_link', 'short_link')
    search_fields = ('name', 'short_link')
    readonly_fields = ('follow_count', 'creation_date')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserModelAdmin)
admin.site.register(Link, LinkModelAdmin)
