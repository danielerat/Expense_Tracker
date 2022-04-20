from django.contrib import admin
from .models import TopUpTransaction, Wallet, Expense,ToDoExpense

# Register your models here.
admin.site.register(TopUpTransaction)
admin.site.register(Wallet)
admin.site.register(Expense)
admin.site.register(ToDoExpense)
