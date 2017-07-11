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
