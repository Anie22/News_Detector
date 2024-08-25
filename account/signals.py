from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import *

@receiver(post_save, sender=UserModel)
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
