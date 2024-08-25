from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import *

# Register your models here.
class MyUserAdmin(BaseUserAdmin):
    list_display = ('full_name', 'email', 'date_joined', 'is_admin', 'is_active')
    search_fields = ('full_name', 'email')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter=('last_login',)
    fieldsets = ()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('full_name', 'user_name', 'email', 'password1', 'password2')
        }),
    )

    ordering=('full_name',)

admin.site.register(UserModel, MyUserAdmin)
admin.site.register(UserProfile)