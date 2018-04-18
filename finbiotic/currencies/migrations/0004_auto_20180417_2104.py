# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0003_auto_20180417_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fill',
            name='fill_text',
            field=models.CharField(max_length=200, verbose_name=b'Market Order, Stop Loss, Take Profit'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_text',
            field=models.CharField(max_length=20, verbose_name=b'Order Type'),
        ),
    ]
