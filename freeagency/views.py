# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import GM, FreeAgent
import requests

def get_image(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    
    url = f'https://nba-players.herokuapp.com//players/{last_name}/{first_name}'
    
    try:
        if (requests.request("GET", url)).text != 'Sorry, that player was not found. Please check the spelling.':
            return url
        return '//imgur.com/RaQJX49'
    except:
        return '//imgur.com/RaQJX49'


def index(request):
    all_fas = FreeAgent.objects.all()
    return render(request, 'freeagency/index.html', {'fas': all_fas})

def userbids(request, username):
    raise NotImplementedError