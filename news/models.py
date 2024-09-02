from django.db import models
from account.models import UserModel

# Create your models here.

class NewsDetector(models.Model):
    news_heading = models.CharField(verbose_name='News Heading', max_length=200, unique=False)
    news_source = models.CharField(verbose_name='News Source', max_length=50, unique=False)
    news_url = models.URLField(verbose_name='News URL', max_length=700, unique=False)
    link_content = models.CharField(verbose_name='Link Content', max_length=500, null=True)
    news_result = models.CharField(verbose_name='Validation Result', max_length=70, default='under going review', blank=True, null=True)
    checked_on = models.DateTimeField(verbose_name='Date Check On', auto_created=True, auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.news_heading

class result(models.Model):
   news_result = models.CharField(verbose_name='Validation Result', max_length=70, default='under going review', blank=True, null=True)
   newsid = models.OneToOneField(NewsDetector, on_delete=models.CASCADE, default=True)
   user = models.ForeignKey(UserModel, on_delete=models.CASCADE, default=True)

   def __str__(self):
       return self.news_result
