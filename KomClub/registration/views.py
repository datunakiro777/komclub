from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def registration(request):
    form = UserCreationForm()
    return render(request, 'registration.html', {'form':form})