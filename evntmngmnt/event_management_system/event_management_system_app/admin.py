from django.contrib import admin
from .models import Event, Category, Attendee

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Attendee)
