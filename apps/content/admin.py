from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, display
from django.utils.html import format_html

from apps.content.models import Post, Score


@admin.register(Post)
class CustomUserAdmin(ModelAdmin):
    model = Post
    list_display = ('title', 'price')
    readonly_fields = ('score_average',)


@admin.register(Score)
class CustomUserAdmin(ModelAdmin):
    model = Score
    list_display = ('score', 'get_username', 'get_post')

    @display(description='username')
    def get_username(self, obj):
        return format_html(f'<a href="/admin/accounts/user/{obj.user.id}/change/">'
                           f'{obj.user.username}'
                           f'</a>')

    @display(description='post')
    def get_post(self, obj):
        return format_html(f'<a href="/admin/content/post/{obj.post.id}/change/">'
                           f'{obj.post.title}'
                           f'</a>')
