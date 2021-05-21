# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import GM, FreeAgent
import requests

def get_image(name: str) -> str:
    first_name = name.split()[0]
    last_name = name.split()[1]
    
    url = f'https://nba-players.herokuapp.com//players/{last_name}/{first_name}'
    
    try:
        if (requests.request("GET", url)).text != 'Sorry, that player was not found. Please check the spelling.':
            return url
        return '//imgur.com/RaQJX49'
    except:
        return '//imgur.com/RaQJX49'

@login_required
def index(request):
    players = FreeAgent.objects.all()
    return render(request, 'freeagency/index.html', {'players': players})

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'freeagency/login.html', {'form': form})

def playerview(request):
    raise NotImplementedError

@login_required
def userbids(request, username):
    bids = GM.objects.get(username=username)
    return render(request, 'freeagency/mybids.html', {'bids': bids})