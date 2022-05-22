from . import views
from django.urls import path

app_name = 'expenses'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('expenses/', views.expenses, name='expenses'),
    path('top_up_transactions/', views.top_up, name='top_up'),
    path('debts/', views.debts, name='debts'),
    # path('home/', views.home, name='home'),
    path('pending_expense/', views.pending_expenses, name='pending_expense'),
]
