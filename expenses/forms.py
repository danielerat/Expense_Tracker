from django.forms import ModelForm
from .models import ToDoExpense


class ToDoExpenseForm(ModelForm):
    class Meta:
        model = ToDoExpense
        fields = ['title', 'description', 'amount', 'date_expected', 'priority']
