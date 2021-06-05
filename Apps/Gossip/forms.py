from django.forms import ModelForm
from .models import Gossip, Character


class Gossipform(ModelForm):
    class Meta:
        model = Gossip
        fields = ['userId','gossipText','pubDate','EndDate','characterId']

class Characterform(ModelForm):
    class Meta:
        model = Character
        fields = ['userId', 'CharacterName']