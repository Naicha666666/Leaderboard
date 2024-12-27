from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeaderboardView.as_view(), name='leaderboard'),
    path('record-match/', views.record_match, name='record_match'),
]