# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 14:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20170709_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the following format: '+999 9999 999'.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
