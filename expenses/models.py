import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
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
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username + ' : ' + self.expense_type + ' (-' + str(self.amount) + ')'


class ToDoExpense(models.Model):
    PRIORITY_TYPE = [
        (1, 'Hign'),
        (2, 'Moderate'),
        (3, 'Low'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(decimal_places=3, max_digits=15, null=False, blank=False)
    date_expected = models.DateTimeField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_TYPE, blank=False, null=False, default=3)
    completed = models.BooleanField(blank=False, null=False, default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.owner.username + '(-' + str(self.amount) + ') On ' + str(self.date_expected.date())
