# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-27 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0177_auto_20190821_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentfileattachment',
            name='scan_resubmit_ttl',
            field=models.IntegerField(default=200),
        ),
    ]
