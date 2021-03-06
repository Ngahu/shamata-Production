# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-29 15:07
from __future__ import unicode_literals

import Main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20171228_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=100)),
                ('image_description', models.TextField()),
                ('gallery_image', models.ImageField(blank=True, null=True, upload_to=Main.models.upload_location)),
            ],
        ),
    ]
