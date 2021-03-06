# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180825_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditHistoryGeneric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_title', models.CharField(max_length=255)),
                ('old_date', models.DateTimeField()),
                ('old_content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='edited',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.EditHistoryGeneric'),
        ),
    ]
