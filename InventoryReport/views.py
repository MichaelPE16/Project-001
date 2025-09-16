from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout





# Create your views here.
""" Home Page"""
def home(request): 
    return render(request, 'home.html')

"""Products Page"""
def products(request):
    if request.method == "POST": 
        pass
    else:
        return render(request, 'products.html')

def clients(request):
    return render(request, 'clients.html')

def sales(request):
    return render(request, 'sales.html')

def sign_in(request):
    return render(request, 'signin.html')

def sign_up(request): 
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def config(request): 
    return render(request, 'config.html')

def log_out(request):
    return HttpResponse('User logout')