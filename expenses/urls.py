from . import views
from django.urls import path

app_name = 'expenses'
urlpatterns = [
    path('', views.home, name='home'),
    path('pending_expense/', views.pending_expenses, name='pending_expense'),
]
