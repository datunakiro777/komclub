from django.urls import path
from clubs.views import my_clubs, clubs

urlpatterns = [
    path('clubs/', clubs),
    path('my_clubs/', my_clubs)
]