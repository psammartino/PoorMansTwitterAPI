from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TweetList, TweetDetail

urlpatterns = [
    path('tweets/', TweetList.as_view()),
    path('tweets/<int:pk>/', TweetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)