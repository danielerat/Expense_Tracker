from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from expenses.models import Wallet
# from django.core.mail import send_mail
# from django.conf import settings
from django.contrib.auth.models import User


# When a user Gets Created, Create him a profile too
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )
        # Create Him A wallet too
        wallet = Wallet.objects.create(owner=profile)

        # Send A welcome Email Message
        # subject = "Welcome To Dev Search"
        # message = "We are glad You are here"
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently=False
        # )


@receiver(post_save, sender=Profile)
def update_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        if profile.email:
            user.email = profile.email
        user.save()
