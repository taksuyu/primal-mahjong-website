from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Event

def event_details_view(request, event_id):
    event = Event.objects.get(id=event_id)

    if event:
        # TODO: Render event page
        pass
    else:
        # TODO: Render not found page
        pass

def event_list_view(request):
    page = request.GET.get('page', 0)
    order = request.GET.get('order', 'start_time') # use '-field' for reverse order
    events = Event.objects.order_by(order)[ page * 9 : 9 ]

    if request.htmx:
        # TODO: Render partial event list
        pass

@login_required
def signup_view(request):
    pass

@login_required
def create_event_view(request):
    pass

@login_required
def edit_event_view(request):
    pass

@login_required
def delete_event_view(request):
    pass