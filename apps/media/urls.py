from django.urls import path

from apps.media.views import MediaDetailAPIView

app_name = 'media'
urlpatterns = [
    path('<int:media_id>', MediaDetailAPIView.as_view(), name='detail')
]
