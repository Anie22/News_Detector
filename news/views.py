from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from news.models import *
from news.detection import *

# Create your views here.

@login_required(login_url='/account/login')
def NewsDetection(request):
    if request.method == 'POST':
        user = request.user
        news_heading = request.POST.get('news_heading').strip().lower()
        news_source = request.POST.get('news_source').strip().lower()
        news_url = request.POST.get('news_url').strip()

        # Get the items from the database for confirmation of existence
        newsCon = NewsDetector.objects.filter(news_heading=news_heading, news_source=news_source, news_url=news_url, user=request.user).exists()

        # A means of identification for the content before submission and saving
        newsIdentification = 'Breaking news'
        ID = newsIdentification.strip().lower()

        # Get the content read from the link or url
        content = get_content_from_link(news_url).strip().lower()
        text = content

        join_words = word_token(text)

        # Get the Gemini AI result
        gemini_result = gemini_prompt(join_words)

        # Checks if the input have been validated by the user before
        if newsCon:
            return JsonResponse({'message':'This content have already been verified by you check history'}, status=404)

        # Checks if the url isn't empty
        if content is None:
            return JsonResponse({'message': 'Unable to retrieve content from the provided URL.'}, status=404)

        # Confirms if the link is a news link
        if ID not in content:
            return JsonResponse({'message': 'The URL needs to be a news link.'}, status=404)

        # Checks if the news heading and source is the same as what is in the link submitted
        if news_heading in content and news_source in content:
            news = NewsDetector.objects.create(news_heading=news_heading, news_source=news_source, news_url=news_url, user=user)
            news.link_content = content
            news.news_result = gemini_result
            news.save()

            # Ensure any previous result is deleted before saving a new one
            result.objects.filter(user=user).delete()

            result_entry = result.objects.create(
                news_result=gemini_result,
                newsid=news,
                user=user
            )
            result_entry.save()

            return JsonResponse({'message':'Saved and under verification'}, status=201)
        else:
            return JsonResponse({'message':'Contents does not match'}, status=404)

    return render(request, 'news.html')

@login_required(login_url='/account/login')
def history(request):
    # Gets all the content in the history
    previous_verifications = NewsDetector.objects.all()

    # Filter and displays the content base on the user making the request
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
    # Gets all the content in the result table
    results = result.objects.all()

    # Filter and displays the content base on the user making the request
    results = result.objects.filter(
        user=request.user,
        newsid__isnull=False,
        news_result__isnull=False
    )
    return render(request, 'results.html', {'results':results})