from django.urls import path
from clubs.views import my_clubs, clubs, create_club

urlpatterns = [
    path('clubs/', clubs),
    path('my_clubs/', my_clubs),
    path('create_club/', create_club)
]