# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBDPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_content', models.TextField()),
                ('title', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'CBD Post',
                'verbose_name_plural': 'CBD Posts',
                'ordering': ('published_at',),
            },
        ),
    ]