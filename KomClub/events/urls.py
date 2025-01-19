from django.urls import path
from events.views import events, create_event, event_detail

urlpatterns = [
    path('events/', events),
    path('create_event/', create_event),
    path('club/<slug:slug>/', event_detail, name='club_detail')
]