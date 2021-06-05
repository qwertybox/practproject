from django.contrib import admin
from .models import *

@admin.register(Gossip)
class GossipAdmin(admin.ModelAdmin):
	list_display = ('id', 'userId','gossipText', 'pubDate', 'characterId')
	list_filter = ('id', 'userId','gossipText', 'pubDate', 'characterId')
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	list_display = ('id', 'userId','CharacterName')