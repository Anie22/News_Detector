from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from news.models import NewsDetector
from news.detection import *

# Create your views here.

@login_required(login_url='/account/login')
def NewsDetection(request):
    if request.method == 'POST':
        user = request.user
        news_heading = request.POST.get('news_heading')
        news_source = request.POST.get('news_source')
        news_url = request.POST.get('news_url')

        heading = NewsDetector.objects.filter(news_heading=news_heading).exists()
        source = NewsDetector.objects.filter(news_source=news_source).exists()
        url = NewsDetector.objects.filter(news_url=news_url).exists()

        if user:
            if heading and source and url:
                return JsonResponse({'message':'This content have already been verified by you check history'}, status=404)
            else:
                news = NewsDetector.objects.create(news_heading=news_heading, news_source=news_source, news_url=news_url, user=user)
                news.content = get_content_from_link(news_url)
                news.save()
                return JsonResponse({'message':'Saved and under verification'}, status=201)
    return render(request, 'news.html')

def history(request):
    return render(request, 'history.html')

def results(request):
    return render(request, 'results.html')