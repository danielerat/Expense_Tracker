from django.forms import ModelForm,Textarea
from .models import ToDoExpense,Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'amount', 'expense_type', 'date']
        widgets = {
            'description': Textarea(attrs={'rows': 2}),
        }
    def __init__(self, *args, **kwargs):
        super(ToDoExpenseForm, self).__init__(*args, **kwargs)
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
