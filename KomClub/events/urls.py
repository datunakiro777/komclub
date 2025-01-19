from django.urls import path
from events.views import events, create_event, event_detail, join_event

urlpatterns = [
    path('events/', events),
    path('create_event/', create_event),
    path('event/<slug:slug>/', event_detail, name='event_detail'),
    path('join_event/<int:id>/', join_event, name='join_event')
]