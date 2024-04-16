from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import logout

from .forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                    
                return redirect('main')
    else:
        form = UserLoginForm()
        
    return render(request, 'users_app/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            user = form.instance
            auth.login(request, user)

            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users_app/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
    