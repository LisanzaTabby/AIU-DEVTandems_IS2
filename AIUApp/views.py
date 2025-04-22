from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic, Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q # allows us our query parameters in one basket so that we can have multiple query and search parameters such we can search using a topic, hostname or roomname
from django.contrib.auth.forms import UserCreationForm
from .forms import RoomForm
# Create your views here.

def loginPage(request):
    page='login' # helps redirect/point a user to the register page or login page
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()# changing it to a lowercase
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist!')

    context={'page':page}
    return render(request, 'AIUApp/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)# saving the form and freezing it in time so that we ca be able to use the username from the form
            user.username = user.username.lower()#updated to alowercase
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error Occured during registration!')
    context={'form':form}
    return render(request, 'AIUApp/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
        )
    room_count = rooms.count()
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))# we are ordering the messages by the created date in descending order
    context={'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'AIUApp/homepage.html', context)
def rooms(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()# we ar telling it get all a specific set of messages related to that specific room.Only for a Many-One R/ship thats when we use the _set.all()Method
    participants = room.participants.all()# we use the all() for the many-Many r/ship
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room= room,
            body= request.POST.get('body')
        )
        room.participants.add(request.user)# adds a user to the participants of a room
        messages.success(request, 'Message sent successfully!')
        return redirect('room', pk=room.id)
    context={'room': room, 'room_messages':room_messages,'participants':participants}
    return render(request, 'AIUApp/room.html', context)
@login_required
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()# we are getting all the rooms that a user has created
    room_messages = user.message_set.all()# we are getting all the messages that a user has sent
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'AIUApp/user_profile.html', context)

@login_required
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)# passing all the data from the form into the cariable form
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user# we are assigning the host of the room to the current user
            room.save()
            messages.success(request, 'Room created successfully!')
            return redirect('home')
    context={'form':form}
    return render(request, 'AIUApp/room_form.html', context)
@login_required
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not the host of this room!')
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)# plus telling it which room to update using the instance variable
        if form.is_valid():
            form.save()
            messages.success(request, 'Room updated successfully!')
            return redirect('home')
    context={'form':form}
    return render(request, 'AIUApp/room_form.html', context)
@login_required
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('You are not the host of this room!')
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully!')
        return redirect('home')
    return render(request, 'AIUApp/delete.html', {'obj':room})
@login_required
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        return HttpResponse('You are not the host of this room!')
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully!')
        return redirect('home')
    return render(request, 'AIUApp/delete.html', {'obj':message})