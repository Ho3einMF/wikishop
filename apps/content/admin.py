from django.contrib import admin

# Register your models here.
from apps.content.models import Post

admin.site.register(Post)

# admin.site.register(Score)
