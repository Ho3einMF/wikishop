from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from apps.accounts.models import User

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
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

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        self.object_id = None

    # these two below functions filter follower and following items to prevent self reference
    # for example a user should not follow self
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.object_id = object_id
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ['follower', 'following']:
            kwargs['queryset'] = User.objects.prevent_self_reference(self.object_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
