import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from django.utils.timezone import now


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=400, blank=True, null=True)
    profile_image = models.ImageField(null=True, upload_to='user_profile', default='user_profile/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username

    @property
    def wallet_balance(self):
        balance = self.wallet.balance
        return balance

    @property
    def monthly_expense(self):
        month = now().month
        expenses = self.expense_set.all()
        monthly = expenses.filter(date__month=month).aggregate(Sum('amount'))

        return monthly['amount__sum']

    @property
    def allowed_expense(self):
        allowed = self.allowedexpense.max_expense
        monthly = self.monthly_expense
        percentage = monthly / allowed * 100
        return {
            'allowed': allowed,
            'percentage': percentage,
        }

    @property
    def get_all_expenses(self):
        expenses = self.expense_set.all()
        total = expenses.aggregate(Sum('amount'))
        return {'total': total['amount__sum'], 'expenses': expenses}

    @property
    def get_pending_expenses(self):
        pending = self.todoexpense_set.all()
        total = pending.aggregate(Sum('amount'))
        count = pending.count()
        return {'count': count, 'pending': pending, 'total': total}

    @property
    def all_top_ups(self):
        month = now().month
        transactions = self.topuptransaction_set.all()
        monthly = transactions.filter(created__month=month)
        monthly_count = monthly.count()
        monthly_sum = monthly.aggregate(Sum('amount'))
        sum = transactions.aggregate(Sum('amount'))
        count = transactions.count()
        return {
            "sum": sum['amount__sum'],
            "count": count,
            "monthly_sum": monthly_sum['amount__sum'],
            "monthly_count": monthly_count,
            'all': transactions,
        }
