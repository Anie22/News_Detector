from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from news.models import NewsDetector
from news.detection import *

# Create your views here.

@login_required(login_url='/account/login')
def NewsDetection(request):
    if request.method == 'POST':
        news_heading = request.POST.get('news_heading')
        news_source = request.POST.get('news_source')
        news_url = request.POST.get('news_url')

        user = request.user

        if news_heading and news_source and news_url:
            news = NewsDetector.objects.create(news_heading=news_heading, news_source=news_source, news_url=news_url, user=user)
            if news_url:
                news.content = get_content_from_link(news_url)
            news.save()
            # messages.success(request, 'Form submitted successfully, await verification')

    return render(request, 'news.html')

