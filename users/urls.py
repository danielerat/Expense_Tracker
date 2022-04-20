from django.urls import path, include
from . import views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
