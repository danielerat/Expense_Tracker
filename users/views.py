from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, "Username or Password Does not Exist")
            return render(request, 'registration/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.warning(request, "Username or Password Does not Exist")
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect('login')


# Create your views here.
def register_user(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        user = CustomUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, "Account Successfully Created")
            return redirect('registration/login.html')
        else:
            messages.info(request, user.errors)

    context = {'form': form}
    return render(request, 'registration/register.html', context)
