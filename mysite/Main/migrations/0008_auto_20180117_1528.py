# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-17 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_auto_20180107_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
