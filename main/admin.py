# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Dish, PriceOption

admin.site.register(Dish)
admin.site.register(PriceOption)
