import os
import nltk
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from news.models import NewsDetector
import google.generativeai as genai

nltk.download('stopwords')
nltk.download('punkt_tab')

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Helps to read through the content of the link
def get_content_from_link(news_url):
    data = requests.get(news_url)
    data_content = BeautifulSoup(data.content, 'html.parser')
    text = data_content.get_text(separator=' ', strip=True)
    token_word = word_token(text)
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
    response = model.generate_content(["Is this news true?", join_words])
    return response.text
