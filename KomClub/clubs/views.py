from django.shortcuts import render
from clubs.forms import ClubsForm
from django.shortcuts import redirect
from clubs.models import Clubs_info
from users.models import User_info

def clubs(request):
    return render(request, 'clubs.html')

def my_clubs(request):
    return render(request, 'myclubs.html')

def create_club(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            form = ClubsForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                Clubs_info.objects.owner = name
                return redirect('/my_clubs')    
    else:
        return redirect('/login')
    form = ClubsForm()
    return render(request, 'create_club.html', {'form': form})
