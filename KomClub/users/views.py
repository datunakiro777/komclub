from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def registration(request):
    if request.method == 'post':
        form = UserCreationForm(request.post)
        if form.is_valid():
            form.save()
        return redirect('')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form':form})