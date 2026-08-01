from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCash
        fields = '__all__'
        exclude = ['user', ]

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user', ]
        