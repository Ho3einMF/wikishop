from django.contrib import admin

from apps.media.models import Media

# Register your models here.

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    # list_display = ('title', 'publish', 'allow_comments', 'comment_count')
    readonly_fields = ['blurhash', 'aspect_ratio']
