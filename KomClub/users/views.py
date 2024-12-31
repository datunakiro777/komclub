from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserInfoForm, LoginForm
from .models import User_info  # Ensure your model includes 'last_name'


def registration(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.last_name = form.cleaned_data['last_name']  # Save the last name
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
            Last_name = form.changed_data['last name']
            password = form.cleaned_data['password']

            try:
                user = User_info.objects.get(username=username, Last_name=Last_name)

                if check_password(password, user.password):
                    request.session['user_id'] = user.id  # Save user ID in session
                    messages.success(request, f"Login successful! Welcome back, {user.last_name}!")
                    return redirect('home')  # Replace 'home' with your desired redirect
                else:
                    messages.error(request, "Invalid password.")
            except User_info.DoesNotExist:
                messages.error(request, "User does not exist.")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
