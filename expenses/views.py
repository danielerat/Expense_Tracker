from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView


@login_required(login_url='login')
def home(request):
    profile = request.user.profile
    wallet = profile.wallet
    context = {'wallet': wallet}
    return render(request, 'expenses/index.html', context)
