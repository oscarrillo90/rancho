# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='menu_category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]