# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-11 11:17
from __future__ import unicode_literals

import Teammembers.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Meamber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to=Teammembers.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
