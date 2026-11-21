from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # USER_TYPE = [('admin', 'Admin'), ('employee', 'Employee')]
    # user_type = models.CharField(max_length=20, default='admin', blank=True)
    pass


from datetime import datetime

class AddCash(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='add_cash')
    source = models.CharField(max_length=256, blank=True, default="")
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.amount}'

class Expense(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expense')
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} - {self.amount}'



class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
