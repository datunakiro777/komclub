from django.urls import path
from clubs.views import my_clubs, clubs, create_club, join_club, club_detail

urlpatterns = [
    path('clubs/', clubs),
    path('my_clubs/', my_clubs),
    path('create_club/', create_club),
    path('join_club/<int:club_id>/', join_club, name='join_club'),
    path('club/<slug:slug>/', club_detail, name='club_detail')
]