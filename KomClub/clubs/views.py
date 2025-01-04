from django.shortcuts import render

# Create your views here.
def clubs(request):
    return render(request, 'clubs.html')

def my_clubs(request):
    return render(request, 'myclubs.html')