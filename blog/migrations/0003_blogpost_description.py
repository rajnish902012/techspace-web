# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-10 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
