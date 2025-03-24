# chat/views.py

from django.shortcuts import render

def chatroom(request):
    return render(request, 'chat/chatroom.html')
