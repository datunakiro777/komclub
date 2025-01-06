from django.shortcuts import render
from clubs.forms import ClubsForm
from django.shortcuts import redirect
from clubs.models import Clubs_info
from users.models import User_info

def clubs(request):
    user_id = request.session.get('user_id')
    if user_id:
        clubs = Clubs_info.objects.all()
    else:
        return redirect('/login')
    return render(request, 'clubs.html', {'clubs': clubs})

def my_clubs(request):
    user_id = request.session.get('user_id')
    if user_id:
        username = request.session.get('username')
        user = User_info.objects.get(username=username)
        clubs = user.clubs.all()
    else:
        return redirect('/login')
    return render(request, 'myclubs.html', {'clubs': clubs})
    
def create_club(request):
    user_id = request.session.get('user_id')
    if user_id:
        if request.method == 'POST':
            form = ClubsForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                club = Clubs_info.objects.get(name=name)
                club.members.add(user_id)
                Clubs_info.objects.update(owner=user_id)
                return redirect('/my_clubs')    
    else:
        return redirect('/login')
    form = ClubsForm()
    return render(request, 'create_club.html', {'form': form})

def join_club(request):
    
    return redirect('/my_clubs')
