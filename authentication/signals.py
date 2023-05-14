from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail
from authentication.models import CustomUser


@receiver(post_save, sender=CustomUser)# sendig welcome email to new users using signal
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to My Site!'
        message = f'Hi {instance.username},\n\nThanks for registering on My Site!'
        from_email = settings.EMAIL_HOST_USER
        to = (instance.email,)
        send_mail(subject, message, from_email, to)
        