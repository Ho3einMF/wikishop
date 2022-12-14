from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from apps.recommend.utils import load_model, sample_recommendation


class UserRecommendationItem(APIView):

    def get(self, request):
        model = load_model()
        sample_recommendation(model, request.User.id)
        print('test')
