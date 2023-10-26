from django.urls import path
from . import views

urlpatterns = [
    path('sentiment_scores', views.sentiment_scores, name='sentiment_scores')
]