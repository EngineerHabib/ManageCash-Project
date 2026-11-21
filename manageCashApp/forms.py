
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import (
    CustomUser,
    AddCash,
    Expense,
    Profile,
)


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
        exclude = ['user']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture',
            'phone',
            'address',
            'bio',
        ]

        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your address',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write something about yourself',
            }),
        }
