from django.shortcuts import render
from .models import Room
# Create your views here.

def index(request):
    rooms = Room.objects.all().order_by('id')
    return render(request, 'AIUApp/homepage.html', {'rooms': rooms})
def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context={'room': room}
    return render(request, 'AIUApp/room.html', context)

