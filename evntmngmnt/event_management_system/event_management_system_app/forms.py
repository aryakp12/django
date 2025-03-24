from django import forms
from .models import Attendee, Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'start_time', 'end_time']

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['event', 'name', 'email']
