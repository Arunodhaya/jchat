# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='sender',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
