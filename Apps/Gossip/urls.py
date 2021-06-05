from django.urls import path, re_path
from . import views
from .views import gossips, addGossip, addCharacter

app_name = 'Gossip'

urlpatterns = [
    path('gossips', gossips, name='gossips'),
    path('addGossip', addGossip, name='addgossip'),
    path('addCharacter', addCharacter, name='addCharacter')
    #path('userid', views.userId, name='userId')
]
