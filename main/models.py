# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models




class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    menu_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PriceOption(models.Model):
    dish = models.ForeignKey(Dish)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    option = models.CharField(max_length=100)

    def __str__(self):
        return self.option
