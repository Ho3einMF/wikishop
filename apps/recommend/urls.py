from django.urls import path

from apps.recommend.views import UserRecommendationItem

urlpatterns = [
    path('user/', UserRecommendationItem.as_view())
]
