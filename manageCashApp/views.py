from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import AddCash, Expense
from .forms import AddCashForm, ExpenseForm
from django.db.models import Sum

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful.")
            return redirect('login_user')
        else:
            return render(request, 'register.html', {'form': form})
    form = RegistrationForm()
    # print(form)
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            # print(user)
            login(request, user)
            messages.success(request, "Login Successful.")
            return redirect('dashboard')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful.")
    return redirect('login_user')


def dashboard(request):
    income = AddCash.objects.aggregate(Sum('amount'))['amount__sum']
    expense = Expense.objects.aggregate(Sum('amount'))['amount__sum']
    context = {
        'income': income,
        'expense': expense,
        'total': income-expense,
    }
    return render(request, 'dashboard.html', context)

def create_addcash(request):
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Income addded successfully.")
            print("DATA SAVED")
            return redirect('dashboard')
        else:
            print(form.errors)
    form = AddCashForm()
    context = {
        'form': form,
        'title': "Add Cash",
        'heading': "Add Cash",
    }
    return render(request, 'base_form.html', context)

def update_addcash(request, id):
    cash_object = get_object_or_404(AddCash, id=id)
    if request.method == 'POST':
        form = AddCashForm(request.POST, instance=cash_object)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Income updated successfully.")
            return redirect('dashboard')
    form = AddCashForm(instance=cash_object)
    context = {
        'form': form,
        'title': "Update Income",
        'heading': "Update Income",
    }
    return render(request, 'base_form.html', context)

def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Expense addded successfully.")
            return redirect('dashboard')
    form = ExpenseForm()
    context = {
        'form': form,
        'title': "Add Expense",
        'heading': "Add Expense",
    }
    return render(request, 'base_form.html', context)

def update_expense(request, id):
    cash_object = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=cash_object)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, "Expense updated successfully.")
            return redirect('dashboard')
    form = ExpenseForm(instance=cash_object)
    context = {
        'form': form,
        'title': "Update Expense",
        'heading': "Update Expense",
    }
    return render(request, 'base_form.html', context)

def delete_addcash(request, id):
    cash_object = get_object_or_404(AddCash, id=id)
    cash_object.delete()
    messages.success(request, "Cash object deleted.")
    return redirect('dashboard')

def delete_expense(request, id):
    cash_object = get_object_or_404(Expense, id=id)
    cash_object.delete()
    messages.success(request, "Cash object deleted.")
    return redirect('dashboard')
