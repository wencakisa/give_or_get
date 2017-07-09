# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 11:47
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Free'), ('R', 'Rent'), ('B', 'Buy')], default='F', max_length=1)),
                ('accepted', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1024)),
                ('phone_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the following format: '+9999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('added_on', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added_on'],
            },
        ),
        migrations.AddField(
            model_name='deal',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
    ]
