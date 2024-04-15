from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                    
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
        
    return render(request, 'users_app/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))