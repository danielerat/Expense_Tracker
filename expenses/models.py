import datetime
import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now
from django.db.models import Sum

from users.models import Profile


class TopUpTransaction(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username + '(+' + str(self.amount) + ')'


# Create your models here.
class Wallet(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(decimal_places=3, max_digits=15, null=False, blank=False, default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username

    # @property
    # def get_latest_topup(self):
    #     transaction = TopUpTransaction.obje
    #     return
    @property
    def monthly_expenses(self):
        month = now().month
        expenses = self.owner.expense_set.filter(date__month=month).aggregate(Sum('amount'))
        return expenses['amount__sum']

    @property
    def get_allowed_Expense(self):
        expenses = self.owner.expense_set.all().aggregate(Sum('amount'))
        return expenses['amount__sum'] @ property

    @property
    def get_all_expenses(self):
        month = now().month
        expenses = self.owner.expense_set.all().aggregate(Sum('amount'))
        return expenses['amount__sum']

    @property
    def get_expense_percentage(self):
        allowed = self.owner.allowedexpense.max_expense
        monthly = self.monthly_expenses
        percentage = monthly / allowed * 100
        return percentage

    @property
    def get_pending_expenses(self):
        pending = self.owner.todoexpense_set.all()
        total = pending.aggregate(Sum('amount'))
        count = pending.count()
        return {'count': count, 'pending': pending, 'total': total}


class AllowedExpense(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    max_expense = models.DecimalField(decimal_places=3, max_digits=15, null=True, blank=False,
                                      validators=[MinValueValidator(Decimal('0.01'))])
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner) + ' :(' + str(self.max_expense) + ')'


class Expense(models.Model):
    EXPENSE_TYPE = [
        ('travel', 'Travel'),
        ('food', 'Food & Grocery'),
        ('phone', 'Cell Phone'),
        ('rent', 'Rent'),
        ('health', 'health & Insurance'),
        ('health', 'health & Insurance'),
        ('clothing', 'Clothing'),
        ('subscription', 'Subscription'),
        ('bill', 'bill'),
        ('other', 'other'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15, null=False, blank=False,
                                 validators=[MinValueValidator(Decimal('0.01'))])
    expense_type = models.TextField(choices=EXPENSE_TYPE, null=False, blank=False)
    date = models.DateField(default=now, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username + ' : ' + self.expense_type + ' (-' + str(self.amount) + ')'


class ToDoExpense(models.Model):
    PRIORITY_TYPE = [
        ('danger', 'High'),
        ('warning', 'Moderate'),
        ('info', 'Low'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15, null=False, blank=False)
    date_expected = models.DateField(default=now, null=False, blank=False)
    priority = models.CharField(max_length=10,choices=PRIORITY_TYPE, blank=False, null=False, default='warning')
    completed = models.BooleanField(blank=False, null=False, default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username + '(-' + str(self.amount) + ') On ' + str(self.date_expected)
