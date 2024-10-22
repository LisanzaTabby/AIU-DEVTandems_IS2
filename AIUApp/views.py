from django.shortcuts import render

# Create your views here.
room_list = [
    {'id':1, 'name':'Lets Learn HTML'},
    {'id':2, 'name':'Lets Learn Python'},
    {'id':3, 'name':'Lets Learn Django'},
]
def index(request):
    return render(request, 'AIUApp/homepage.html', {'rooms': room_list})
def rooms(request, pk):
    room = None
    for i in room_list:
        if i['id'] == int(pk):
            room = i

    context={'room': room}
    return render(request, 'AIUApp/room.html', context)

