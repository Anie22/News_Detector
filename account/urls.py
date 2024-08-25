from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', loginView, name='login'),
    path('logout/', logout_view, name='logout')
]