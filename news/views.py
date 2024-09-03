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
        news_heading = request.POST.get('news_heading').strip().lower()
        news_source = request.POST.get('news_source').strip().lower()
        news_url = request.POST.get('news_url').strip()

        newsCon = NewsDetector.objects.filter(news_heading=news_heading, news_source=news_source, news_url=news_url, user=request.user).exists()

        if newsCon:
            return JsonResponse({'message':'This content have already been verified by you check history'}, status=404)

        content = get_content_from_link(news_url).strip().lower()
        if content is None:
            return JsonResponse({'message': 'Unable to retrieve content from the provided URL.'}, status=404)

        if news_heading in content and news_source in content:
            news = NewsDetector.objects.create(news_heading=news_heading, news_source=news_source, news_url=news_url, user=user)
            news.link_content = content
            news.save()
            return JsonResponse({'message':'Saved and under verification'}, status=201)
        else:
            return JsonResponse({'message':'Contents does not match'}, status=404)

    return render(request, 'news.html')

@login_required(login_url='/account/login')
def history(request):
    previous_verifications = NewsDetector.objects.all()

    previous_verifications = NewsDetector.objects.filter(
        user=request.user,
        news_heading__isnull=False,
        news_source__isnull=False,
        news_url__isnull=False,
        link_content__isnull=False,
        news_result__isnull=False,
        checked_on__isnull=False,
    )
    return render(request, 'history.html', {'previous_verifications':previous_verifications})

@login_required(login_url='/account/login')
def results(request):
    return render(request, 'results.html')