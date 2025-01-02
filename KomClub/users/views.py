from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserInfoForm, LoginForm
from users.models import User_info
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def register(request):
    if request.user.is_authenticated:
        return redirect('')
    
    else:
        if request.method == 'POST':
            form = UserInfoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')
        else:
            form = UserInfoForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm(request.POST)
        if request.method == 'POST':
           if form.is_valid():
               username = form.cleaned_data['username']
               last_name = form.cleaned_data['last_name']
               password = form.cleaned_data['password']
               user = authenticate(username=username, last_name=last_name, password=password)
               if user:
                   return redirect('/')
               else:
                   return HttpResponse('Username or Password is incorrect')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    user_registered = False
    return redirect('/', {'user_Registered': user_registered}) 
            
