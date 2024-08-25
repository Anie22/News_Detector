from django.urls import path
from django.contrib.auth.decorators import login_required
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', login_required(NewsDetection), name='news_app')
]