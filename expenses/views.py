from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Expense, Wallet, Profile, TopUpTransaction
from .forms import ToDoExpenseForm


def tester(request):
    page_name = 'Dashboard'
    # user_id = request.user.profile.id
    # profile = Profile.objects.select_related('wallet').get(id=user_id)
    profile = request.user.profile
    context = {'profile': profile, }
    return render(request, 'expenses/tester.html', context)


@login_required(login_url='login')
def home(request):
    page_name = 'Dashboard'
    profile = request.user.profile
    # wallet = profile.wallet
    last_transaction = profile.topuptransaction_set.last().amount
    context = {'profile': profile, 'page_name': page_name, 'last_transaction': last_transaction}
    return render(request, 'expenses/index.html', context)


def pending_expenses(request):
    form = ToDoExpenseForm()
    page_name = 'Pending Expenses'
    profile = request.user.profile
    expenses = profile.todoexpense_set.all()
    context = {'page_name': page_name, 'pending_expenses': expenses, 'form': form}
    return render(request, 'expenses/pending_expenses_list.html', context)
