from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Profile
from authentication.models import CustomUser

@receiver(post_save, sender=CustomUser)
def setprofile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
