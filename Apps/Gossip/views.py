from django.shortcuts import render
from .models import *

from django.http import HttpResponse, Http404
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .forms import Gossipform, Characterform


# Create your views here.


def gossips(request):
    currentuser = request.user  
    allGossips = Gossip.objects.all().order_by('-pubDate')
    d = []
    gossips = Gossip.objects.values('id').distinct()
    for gossip in allGossips:
        if getattr(gossip, 'userId') == currentuser.id:
            d.append(gossip['id'])
    userGossips = Gossip.objects.all().filter(id__in=d).order_by('-pubDate')


    context = {
        "allGossips" : allGossips,
        "userGossips" : userGossips,
        "user" : currentuser,
    }
    return render(request, 'gossips.html', context)
def addGossip(request):
    if request.method == 'POST':
        form = Gossipform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Gossipform()
    context = {
        'form': form,
    }
    return render(request, 'addgossip.html', context=context)
def addCharacter(request):
    if request.method == 'POST':
        form = Characterform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Characterform()
    context = {
        'form': form,
    }
    return render(request, 'addCharacter.html', context=context)