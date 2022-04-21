from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Expense


@login_required(login_url='login')
def home(request):
    profile = request.user.profile
    wallet = profile.wallet
    last_transaction = wallet.owner.topuptransaction_set.last()
    context = {'wallet': wallet, 'last_transaction': last_transaction}
    return render(request, 'expenses/index.html', context)
