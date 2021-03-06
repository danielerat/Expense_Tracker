from django.forms import ModelForm, Textarea
from .models import ToDoExpense, Expense, Debt, TopUpTransaction


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'amount', 'expense_type', 'date']
        widgets = {
            'description': Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        # The fast way
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ToDoExpenseForm(ModelForm):
    class Meta:
        model = ToDoExpense
        fields = ['title', 'description', 'amount', 'date_expected', 'priority']
        widgets = {
            'description': Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(ToDoExpenseForm, self).__init__(*args, **kwargs)
        # The fast way
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class TopUpForm(ModelForm):
    class Meta:
        model = TopUpTransaction
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        super(TopUpForm, self).__init__(*args, **kwargs)
        # The fast way
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class DebtForm(ModelForm):
    class Meta:
        model = Debt
        fields = ['title', 'amount', 'date_expected']

    def __init__(self, *args, **kwargs):
        super(DebtForm, self).__init__(*args, **kwargs)
        # The fast way
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
