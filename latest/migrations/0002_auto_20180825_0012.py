# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 18:42
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('latest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestpost',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name=b'image'),
        ),
    ]
