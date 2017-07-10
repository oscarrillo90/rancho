# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


def __str__(self):
		return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
