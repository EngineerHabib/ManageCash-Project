
from django.urls import path
from .views import *

urlpatterns = [
    path('', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),

    path('dashboard/', dashboard, name='dashboard'),
    path('create_addcash/', create_addcash, name='create_addcash'),
    path('update_addcash/<str:id>/', update_addcash, name='update_addcash'),
    path('create_expense/', create_expense, name='create_expense'),
    path('update_expense/<str:id>/', update_expense, name='update_expense'),
    path('delete_addcash/<str:id>/', delete_addcash, name='delete_addcash'),
    path('delete_expense/<str:id>/', delete_expense, name='delete_expense'),

    # Profile Management
    path('profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
