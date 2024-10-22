from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'homepage.html', context)
def rooms(request):
    context={}
    return render(request, 'room.html', context)

