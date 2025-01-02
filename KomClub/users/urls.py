from django.urls import path
from users.views import register, login, logout_view

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout_view)
]