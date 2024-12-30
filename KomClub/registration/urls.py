from django.urls import path
from registration.views import registration

urlpatterns = [
    path('', registration)
]