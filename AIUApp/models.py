from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg", blank=True)
    
    # user socials
    linkedin = models.URLField(max_length=300, null=True, blank=True)
    github = models.URLField(max_length=300, null=True, blank=True)
    stackoverflow = models.URLField(max_length=300, null=True, blank=True)
    twitter = models.URLField(max_length=300, null=True, blank=True)

    # New fields for career/developer profile
    skills = models.TextField(null=True, blank=True, help_text="List of skills, separated by commas (e.g. Python, Django, React)")
    experience = models.TextField(null=True, blank=True, help_text="Describe projects, internships, or work experience")
    goals = models.TextField(null=True, blank=True, help_text="Describe your learning goals and areas to improve")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # fields that are required when creating a user

class Topic(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic= models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # takes the timestamp if a model is changed
    created = models.DateTimeField(auto_now_add=True)# takes timestamp of when the model item was created

    class Meta:
        ordering = ["-updated","-created"]

    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #link it to the parent model Room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated","-created"]

    def __str__(self):
        return self.body[0:50] # returns the first 50 characters of the message body
