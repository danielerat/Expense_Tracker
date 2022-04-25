from django.forms import ModelForm
from .models import ToDoExpense


class ToDoExpenseForm(ModelForm):
    class Meta:
        model = ToDoExpense
        fields = ['title', 'description', 'amount', 'date_expected', 'priority']
        # widgets = {
        #     'date_expected': ModelForm.RadioSelect
        # }
    def __init__(self, *args, **kwargs):
        super(ToDoExpenseForm, self).__init__(*args, **kwargs)
        # The fast way
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
