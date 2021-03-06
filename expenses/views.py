from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ToDoExpenseForm, ExpenseForm, TopUpForm, DebtForm
from .models import TopUpTransaction


def test(request):
    page_name = 'Dashboard'
    # user_id = request.user.profile.id
    # profile = Profile.objects.select_related('wallet').get(id=user_id)
    profile = request.user.profile
    transaction = profile.all_top_ups

    context = {'transaction': transaction, }
    return render(request, 'expenses/tester.html', context)


@login_required(login_url='login')
def home(request):
    page_name = 'Dashboard'
    profile = request.user.profile
    # wallet = profile.wallet
    last_transaction = profile.topuptransaction_set.last().amount

    # Get All Expenses and their Total
    expenses = profile.get_all_expenses

    # Get Allowed Expenses
    allowed_expense = profile.allowed_expense

    # Getting pending All pending expenses, their count and total
    pending = profile.get_pending_expenses

    context = {'profile': profile, 'page_name': page_name, 'last_transaction': last_transaction,
               'pending': pending, 'allowed_expense': allowed_expense, 'expenses': expenses}
    return render(request, 'expenses/index.html', context)


def pending_expenses(request):
    form = ToDoExpenseForm()
    page_name = 'Pending Expenses'
    if request.method == 'POST':
        pending = ToDoExpenseForm(request.POST)
        if pending.is_valid():
            p = pending.save(commit=False)
            p.owner = request.user.profile
            p.save()
            messages.success(request,
                             "Hey %s, Your Pending Expense is successfully saved" % request.user.profile.first_name)
            return redirect("expenses:pending_expense")
        else:
            form = pending

    profile = request.user.profile
    expenses = profile.todoexpense_set.all().order_by("-created")
    context = {'page_name': page_name, 'pending_expenses': expenses, 'form': form}
    return render(request, 'expenses/pending_expenses_list.html', context)


def expenses(request):
    form = ExpenseForm()
    page_name = 'Expenses'
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            e = expense.save(commit=False)
            e.owner = request.user.profile
            e.save()
            messages.success(request,
                             "Hey %s, Your Expense is successfully saved" % request.user.profile.first_name)
            return redirect("expenses:expenses")
        else:
            print(expense.errors)
            note = "Error While saving the pending expense"
            form = expense

    profile = request.user.profile
    expenses = profile.expense_set.all().order_by("-created")
    context = {'page_name': page_name, 'expenses': expenses, 'form': form}
    return render(request, 'expenses/expenses.html', context)


def top_up(request):
    form = TopUpForm()
    page_name = 'Top Up Transactions'
    if request.method == 'POST':
        t_transaction = TopUpForm(request.POST)
        if t_transaction.is_valid():
            t = t_transaction.save(commit=False)
            t.owner = request.user.profile
            t.save()
            messages.success(request,
                             "Hey %s, You successfully Added Money To your wallet" % request.user.profile.first_name)
            return redirect("expenses:top_up")
        else:
            print(t_transaction.errors)
            print(request.POST)
            note = "Error While saving the pending expense"
            form = t_transaction

    profile = request.user.profile
    transactions = profile.all_top_ups
    context = {'page_name': page_name, 'profile': profile, 'transactions': transactions, 'form': form}
    return render(request, 'expenses/topup.html', context)


def debts(request):
    form = DebtForm()
    page_name = 'Who owe you money?'

    if request.method == 'POST':
        t_transaction = TopUpForm(request.POST)
        if t_transaction.is_valid():
            t = t_transaction.save(commit=False)
            t.owner = request.user.profile
            t.save()
            messages.success(request,
                             "Hey %s, You successfully Added Money To your wallet" % request.user.profile.first_name)
            return redirect("expenses:debts")
        else:
            print(t_transaction.errors)
            print(request.POST)
            note = "Error While saving the pending expense"
            form = t_transaction

    profile = request.user.profile
    debts = profile.debt_set.filter(paid=False).order_by('-created')
    all_debts = profile.all_debts
    context = {'page_name': page_name, 'all_debts': all_debts, 'debts': debts, 'profile': profile, 'form': form}
    return render(request, 'expenses/debt.html', context)
