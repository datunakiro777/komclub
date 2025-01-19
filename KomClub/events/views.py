from django.shortcuts import render
from users.models import User_info
from django.shortcuts import redirect
from events.forms import CreateEventForm
from django.shortcuts import render
from events.models import Events
from django.http import HttpResponse

def events(request):
    user_id = request.session.get('user_id')
    if user_id:
        events = Events.objects.all()
    else:
        redirect('/login')
    return render(request, 'events.html', {'events': events})

def create_event(request):
    user_id = request.session.get('user_id')
    user = User_info.objects.get(id=user_id)
    form = CreateEventForm()
    if user.premmision == True:
        if request.method == 'POST':
            form = CreateEventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/events') 
            else:
                return HttpResponse('somethings invalid')
    else:
        return HttpResponse('you do not have a premmision to create an event contact us on facebook or instagram for premmision')
    
    return render(request, 'create_event.html', {'form' : form})

def event_detail(request, slug):
    return render(request, 'event_detail.html')