# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-01 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20180919_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='display_order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
