from django.shortcuts import render, get_object_or_404
from .models import Event, Category, Attendee
from .forms import AttendeeForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    form = AttendeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'event_detail.html', {'event': event, 'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
