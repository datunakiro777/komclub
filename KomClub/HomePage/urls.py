from django.urls import path
from HomePage.views import home
urlpatterns = [
    path('', home, name='home')
]