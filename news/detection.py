import os
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from news.models import NewsDetector
import google.generativeai as genai

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Helps to read through the content of the link
def get_content_from_link(news_url):
    data = requests.get(news_url)
    link = NewsDetector.objects.filter(news_url=news_url).exists()
    data_content = BeautifulSoup(data.content, 'html.parser')
    text = data_content.get_text(separator='', strip=True)
    token_word = word_token(text)

    print(token_word)

    # saves the content from the link
    if link:
        content = NewsDetector.objects.get(news_url=link)
        content.link_content = token_word
        content.save()

    return token_word

#
def word_token(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    word_text = [word for word in words if word.isalnum() and word not in stop_words]
    join_words = ' '.join(word_text)
    gemini_prompt(join_words)
    return text

# Sends the generated prompt to gemini
def gemini_prompt(join_words):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["Is this news true", join_words, "compare it with other reliable news sources in the world and Nigeria and return a result from them"])
    return response.text
