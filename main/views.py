# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Dish, PriceOption



def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def menu(request):
    dishes = Dish.objects.all()
    print(dishes)
    return render(request, 'menu.html', {'dishes': dishes})

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')




def appetizers(request):
    appetizers = Dish.objects.filter(menu_category='appetizer')
    priceOptions = PriceOption.objects.all()
    print(appetizers)
    print("Price Options: " , priceOptions)
    return render(request, 'appetizers.html', {'appetizers': appetizers, 'priceOptions': priceOptions})

def soupSalad(request):
    soupSalad = Dish.objects.filter(menu_category='soup/salad')
    priceOptions = PriceOption.objects.all()
    print(soupSalad)
    print("Price Options: " , priceOptions)
    return render(request, 'soup-salad.html', {'soupSalad': soupSalad, 'priceOptions': priceOptions})

def texmex(request):
    texmex = Dish.objects.filter(menu_category='texmex')
    priceOptions = PriceOption.objects.all()
    print(texmex)
    print("Price Options: " , priceOptions)
    return render(request, 'texmex.html', {'texmex': texmex, 'priceOptions': priceOptions})

def entrees(request):
    entrees = Dish.objects.filter(menu_category='entrees')
    priceOptions = PriceOption.objects.all()
    print(entrees)
    print("Price Options: " , priceOptions)
    return render(request, 'entrees.html', {'entrees': entrees, 'priceOptions': priceOptions})

def mexican(request):
    mexican = Dish.objects.filter(menu_category='mexican')
    priceOptions = PriceOption.objects.all()
    print(mexican)
    print("Price Options: " , priceOptions)
    return render(request, 'mexican.html', {'mexican': mexican, 'priceOptions': priceOptions})

def kids(request):
    kids = Dish.objects.filter(menu_category='kids')
    priceOptions = PriceOption.objects.all()
    print(kids)
    print("Price Options: " , priceOptions)
    return render(request, 'kids.html', {'kids': kids, 'priceOptions': priceOptions})

def lunch(request):
    lunch = Dish.objects.filter(menu_category='lunch')
    priceOptions = PriceOption.objects.all()
    print(lunch)
    print("Price Options: " , priceOptions)
    return render(request, 'lunch.html', {'lunch': lunch, 'priceOptions': priceOptions})
