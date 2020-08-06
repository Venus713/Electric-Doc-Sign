from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Administrator


class FannabisUserAdmin(UserAdmin):
    model = User
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

class AdministratorAdmin(FannabisUserAdmin):
    model = Administrator


admin.site.site_header = _('DocSign Shop administration')
admin.site.site_title = _('DocSign Shop administration')
admin.site.index_title = _('Shop administration')
admin.site.register(Administrator, AdministratorAdmin)
