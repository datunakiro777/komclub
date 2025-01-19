from django.shortcuts import render
from clubs.forms import ClubsForm, CommentForm
from django.shortcuts import redirect
from clubs.models import Clubs_info, Comments
from users.models import User_info
from django.http import HttpResponse
from django.db.models import Count
import datetime

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

def join_club(request, club_id):
    user_id = request.session.get('user_id')
    if user_id:
        club = Clubs_info.objects.get(id=club_id)
        if club.members.filter(id=user_id).exists():
            return HttpResponse('already joined')
        else:
            club.members.add(user_id)
            return redirect('/my_clubs')
    else:
        redirect('/login')


def club_detail(request, slug):
    user_id = request.session.get('user_id')
    if user_id:
        club = Clubs_info.objects.get(slug=slug)
        comments = club.club_comments.all()
        form = CommentForm()
        members_count = club.members.aggregate(members_count=Count('id'))
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                text = form.cleaned_data['text']
                Comments.objects.filter(text=text).update(user=user_id)
    else:
        return redirect('/login')
    return render(request, 'club_detail.html', {'club' : club, 'members_count' : members_count, 'form' : form, 'comments': comments})


def leave_club(request, club_id):
    club = Clubs_info.objects.get(id=club_id)
    user_id = request.session.get('user_id')
    club.members.remove(user_id)
    return redirect('/my_clubs')

    