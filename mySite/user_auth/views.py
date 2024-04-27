#user_auth/views
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')  # Redirect to your home page or another view
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'user_auth/signin.html', {'form': form})
 
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page or another view
    else:
        form = RegistrationForm()
    return render(request, 'user_auth/register.html', {'form': form})
 

