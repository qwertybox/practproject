import json
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, timedelta

class Character(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    CharacterName = models.TextField(max_length=500)
    def __str__(self):
        """
        Строка для представления character
        """
        return self.CharacterName
    def __int__(self):
        """
        Получаем id gossip
        """
        return self.id

class Gossip(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    gossipText = models.TextField(max_length=4000)
    pubDate = models.DateTimeField(default=timezone.now)
    EndDate = models.DateTimeField(default=timezone.now)
    characterId = models.ForeignKey(Character, on_delete=models.CASCADE) 
    #interval = models.CharField(max_length=128) можна обійтися без нього
    def __str__(self):
        """
        Строка для представления gossip
        """
        return self.gossipText
    def __int__(self):
        """
        Получаем id gossip
        """
        return self.id
#	def get_absolute_url(self):
#		return reverse('Gossip', args=[str(self.id)])