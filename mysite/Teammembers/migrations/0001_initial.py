# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-29 12:26
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
                ('members_name', models.CharField(max_length=100)),
                ('members_role', models.CharField(max_length=100)),
                ('slug_name', models.SlugField(unique=True)),
                ('members_details', models.TextField()),
                ('members_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True)),
                ('members_email', models.EmailField(max_length=254)),
                ('members_image', models.ImageField(upload_to=Teammembers.models.upload_location)),
            ],
        ),
    ]
