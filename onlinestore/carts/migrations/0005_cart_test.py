# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20160127_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='test',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], default='color', max_length=120),
            preserve_default=False,
        ),
    ]
