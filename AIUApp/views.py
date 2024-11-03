from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

def index(request):
    rooms = Room.objects.all()
    return render(request, 'AIUApp/homepage.html', {'rooms': rooms})
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



