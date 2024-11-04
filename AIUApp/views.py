from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q # allows us our query parameters in one basket so that we can have multiple query and search parameters such we can search using a topic, hostname or roomname
from .forms import RoomForm
# Create your views here.

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context={'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'AIUApp/homepage.html', context)
def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context={'room': room}
    return render(request, 'AIUApp/room.html', context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)# passing all tghe data from the form into the cariable form
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'AIUApp/room_form.html', context)
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)# plus telling it which room to update using the instance variable
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'AIUApp/room_form.html', context)
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'AIUApp/delete.html',{'obj':room})



