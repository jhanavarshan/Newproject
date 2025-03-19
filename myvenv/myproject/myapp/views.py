from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def production(request):
    return render(request, 'production.html')

def dovegel(request):
    return render(request, 'dovegel.html')

def inventory(request):
    return render(request, 'inventory.html')

def products(request):
    return render(request, 'products.html')

def rawmaterials(request):

    return render(request, 'rawmaterials.html')
