from django.urls import path
from users.views import registration

urlpatterns = [
    path('', registration)
]