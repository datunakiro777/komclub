from django.urls import path
from users.views import registration, login_view

urlpatterns = [
    path('register/', registration),
    path('login/', login_view)
]