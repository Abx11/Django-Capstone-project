# user_auth/urls.py
from django.urls import path
from .views import user_login, user_register

app_name = 'user_auth'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    # Add other authentication-related views as needed
]
