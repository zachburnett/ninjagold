from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,'login_app/index.html')

def register(request):
    results = User.objects.Regval(request.POST)
    if results['status'] == False: 
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    user = User.objects.creator(request.POST)    
    messages.success(request, 'user has been created. login to continue')
    return redirect('/')

def login(request):
    results = User.objects.loginval(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = results['user'].id
    return redirect('/gold')