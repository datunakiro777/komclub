from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .forms import UserInfoForm
from .forms import LoginForm
from .models import User_info

def registration(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            
            return redirect('/')
    else:
        form = UserInfoForm()

    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User_info.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id  # Save user ID in session
                    messages.success(request, "Login successful!")
                    return redirect('home')  # Replace 'home' with your desired redirect
                else:
                    messages.error(request, "Invalid password.")
            except User_info.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
