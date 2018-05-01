# from django.http import HttpResponse
from django.shortcuts import render, redirect

def welcome(requset):
    # return HttpResponse("Hello, Jay")
    if requset.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(requset, 'player/welcome.html')
