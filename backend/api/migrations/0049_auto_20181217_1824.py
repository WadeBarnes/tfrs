# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-17 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20181213_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentfileattachment',
            name='url',
            field=models.URLField(max_length=2048),
        ),
    ]
