from django.urls import path
from users.views import register, login

urlpatterns = [
    path('register/', register),
    path('login/', login)
]