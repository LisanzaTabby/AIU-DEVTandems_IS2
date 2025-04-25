from django import forms
from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'E.g. Mastering ES6-JavaScript', 'class': 'form__group','id': 'room-name'}),
            'topic': forms.Select(attrs={'class': 'form__group','id': 'room-topic'}),
            'description': forms.Textarea(attrs={'placeholder': 'E.g. This is a room for learning ES6-JavaScript', 'class': 'form__group','id': 'room_about'}),
        }
        labels = {
            'name': 'Room Name',
            'topic': 'Topic',
            'description': 'Room Description',
        }
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        