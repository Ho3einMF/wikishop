from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.accounts.forms import UserModelForm
from apps.accounts.models import User, Session

admin.site.unregister(Group)

admin.site.register(Session)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    form = UserModelForm
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'last_login', 'date_joined')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Profile', {'fields': ('first_name', 'last_name', 'avatar', 'bio', 'follower', 'following')}),
        ('Saved Posts', {'fields': ('saved_posts',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined', 'last_login')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('username',)
    ordering = ('email',)
