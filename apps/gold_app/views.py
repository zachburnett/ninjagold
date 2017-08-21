from django.shortcuts import render,redirect
from ..login_app.models import User
from django.db.models import Sum
from .models import Game
import random
# Create your views here.
def index(request):
    
    context ={
        'top5' : User.objects.all().order_by('-total')[:5],
             
    }
    return render(request,'gold_app/index.html',context)

def play(request):
    user = User.objects.get(id = request.session['user_id'])
    context = {'total': user.total, 'games': user.games.all().order_by('-created_at')}
    print context 
    return render(request,'gold_app/play.html', context)

def process(request):
    current_user = User.objects.get(id = request.session['user_id'])
    if request.POST['building'] == 'cave':
        gold = random.randint(0,3)
        chance = random.randint(0,1)
        if chance == 0:
            Game.objects.creategame(current_user, -gold)
            print Game.objects.all(), gold 
            
        else:
            Game.objects.creategame(current_user, gold)
            score = 0
            for x in current_user.games.all():
                score += x.gold 
            current_user.total = score 
            current_user.save()    
            
    if request.POST['building'] == 'barn':
        gold = random.randint(0,8)
        chance = random.randint(0,1)
        if chance == 0:
            Game.objects.creategame(current_user, -gold)
        else:
            Game.objects.creategame(current_user, gold)
            score = 0
            for x in current_user.games.all():
                score += x.gold
            current_user.total = score
            current_user.save()
    
    if request.POST['building'] == 'river':
        gold = random.randint(0,15)
        chance = random.randint(0,1)
        if chance == 0:
            Game.objects.creategame(current_user, -gold)
        else:
            Game.objects.creategame(current_user, gold)
            score = 0
            for x in current_user.games.all():
                score += x.gold
            current_user.total = score
            current_user.save()

    if request.POST['building'] == 'steal_gold':
        gold = random.randint(0,100)
        chance = random.randint(0,1)
        if chance == 0:
            Game.objects.creategame(current_user, -gold)
        else:
            Game.objects.creategame(current_user, gold)
            score = 0
            for x in current_user.games.all():
                score += x.gold
            current_user.total = score
            current_user.save()
    return redirect('/gold/play')

def show(request):
    x = User.objects.get(id = request.session['user_id'])
    context = {
        'users': User.objects.all(),    
        
    }
    print User.objects.all()
    return render(request,'gold_app/show.html',context)

def showplayer(request, user_id):
    context ={
        'user':  User.objects.get(id = user_id)
    }
    return render(request,'gold_app/showplay.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')