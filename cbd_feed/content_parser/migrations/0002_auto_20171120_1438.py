# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cbdpost',
            options={'ordering': ('-published_at',), 'verbose_name': 'CBD Post', 'verbose_name_plural': 'CBD Posts'},
        ),
    ]
