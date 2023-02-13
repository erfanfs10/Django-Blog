from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from core.models import Profile


@receiver(post_save, sender=User)
def setprofile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
