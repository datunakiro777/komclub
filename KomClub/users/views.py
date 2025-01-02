from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .forms import UserInfoForm, LoginForm
from users.models import User_info
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def register(request):
    user_id = request.session.get('user_id')
    if request.user.is_authenticated:
        return redirect('/')
    
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
    user_id = request.session.get('user_id')
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            gmail = form.cleaned_data['gmail']

            try:
                user = User_info.objects.filter(gmail=gmail, password=password)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return redirect('/')
                else:
                    return HttpResponse('Invalid username or password')
            except User_info.DoesNotExist:
                return HttpResponse('User does not exist')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/') 
            
