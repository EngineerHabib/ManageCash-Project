
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import CustomUser, AddCash, Expense, Profile
from .forms import (
    RegistrationForm,
    LoginForm,
    AddCashForm,
    ExpenseForm,
    ProfileForm,
)


# =========================
# USER REGISTRATION
# =========================

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)

            messages.success(request, "Registration Successful.")
            return redirect('login_user')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


# =========================
# USER LOGIN
# =========================

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, "Login Successful.")
            return redirect('dashboard')
    else:
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})


# =========================
# USER LOGOUT
# =========================

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successful.")
    return redirect('login_user')


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    income = AddCash.objects.filter(
        user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    expense = Expense.objects.filter(
        user=request.user
    ).aggregate(total=Sum('amount'))['total'] or 0

    context = {
        'income': income,
        'expense': expense,
        'total': income - expense,
    }

    return render(request, 'dashboard.html', context)


# =========================
# ADD CASH
# =========================

@login_required
def create_addcash(request):

    if request.method == 'POST':
        form = AddCashForm(request.POST)

        if form.is_valid():
            cash = form.save(commit=False)
            cash.user = request.user
            cash.save()

            messages.success(request, "Income added successfully.")
            return redirect('dashboard')
    else:
        form = AddCashForm()

    context = {
        'form': form,
        'title': "Add Cash",
        'heading': "Add Cash",
    }

    return render(request, 'base_form.html', context)


# =========================
# UPDATE CASH
# =========================

@login_required
def update_addcash(request, id):

    cash_object = get_object_or_404(
        AddCash,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = AddCashForm(request.POST, instance=cash_object)

        if form.is_valid():
            form.save()

            messages.success(request, "Income updated successfully.")
            return redirect('dashboard')
    else:
        form = AddCashForm(instance=cash_object)

    context = {
        'form': form,
        'title': "Update Income",
        'heading': "Update Income",
    }

    return render(request, 'base_form.html', context)


# =========================
# ADD EXPENSE
# =========================

@login_required
def create_expense(request):

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

            messages.success(request, "Expense added successfully.")
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    context = {
        'form': form,
        'title': "Add Expense",
        'heading': "Add Expense",
    }

    return render(request, 'base_form.html', context)


# =========================
# UPDATE EXPENSE
# =========================

@login_required
def update_expense(request, id):

    expense_object = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense_object)

        if form.is_valid():
            form.save()

            messages.success(request, "Expense updated successfully.")
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense_object)

    context = {
        'form': form,
        'title': "Update Expense",
        'heading': "Update Expense",
    }

    return render(request, 'base_form.html', context)


# =========================
# DELETE CASH
# =========================

@login_required
def delete_addcash(request, id):

    cash_object = get_object_or_404(
        AddCash,
        id=id,
        user=request.user
    )

    cash_object.delete()

    messages.success(request, "Cash object deleted.")
    return redirect('dashboard')


# =========================
# DELETE EXPENSE
# =========================

@login_required
def delete_expense(request, id):

    expense_object = get_object_or_404(
        Expense,
        id=id,
        user=request.user
    )

    expense_object.delete()

    messages.success(request, "Expense deleted successfully.")
    return redirect('dashboard')


# =========================
# VIEW PROFILE
# =========================

@login_required
def view_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    context = {
        'profile': profile,
        'user': request.user,
    }

    return render(request, 'profile.html', context)


# =========================
# EDIT PROFILE
# =========================

@login_required
def edit_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit_profile.html', context)
