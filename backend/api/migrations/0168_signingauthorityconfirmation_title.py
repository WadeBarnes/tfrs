# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-06 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0167_compliancereporthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='signingauthorityconfirmation',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
