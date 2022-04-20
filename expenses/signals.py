from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import TopUpTransaction, Wallet, Expense
from django.contrib.auth.models import User


# WHen there is a TopUp Transaction , then simply Add the Amount in User Wallet balance
@receiver(post_save, sender=TopUpTransaction)
def create_profile(sender, instance, created, **kwargs):
    if created:
        top_up = instance

        wallet = Wallet.objects.get(owner=top_up.owner)
        wallet.balance = wallet.balance + top_up.amount
        wallet.save()
    else:
        pass


# When There is AN expense , remove money from wallet
@receiver(post_save, sender=Expense)
def create_profile(sender, instance, created, **kwargs):
    if created:
        expense = instance
        wallet = Wallet.objects.get(owner=expense.owner)
        wallet.balance = wallet.balance - expense.amount
        wallet.save()
    else:
        pass

# @receiver(post_save, sender=Profile)
# def update_profile(sender, instance, created, **kwargs):
#     profile = instance
#     user = profile.user
#     if not created:
#         user.first_name = profile.first_name
#         user.last_name = profile.last_name
#         user.username = profile.username
#         if profile.email:
#             user.email = profile.email
#         user.save()
