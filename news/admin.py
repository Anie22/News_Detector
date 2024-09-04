from django.contrib import admin
from news.models import NewsDetector, result

# Register your models here.
admin.site.register(NewsDetector)
admin.site.register(result)