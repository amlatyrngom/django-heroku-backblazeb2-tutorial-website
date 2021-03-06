# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_bio', models.TextField(max_length=512)),
                ('picture', models.ImageField(default='members/py.png', upload_to='members')),
            ],
        ),
    ]
