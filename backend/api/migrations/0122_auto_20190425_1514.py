# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0121_add_fuel_class_relationships'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultcarbonintensitycategory',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defaultcarbonintensitycategory',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energydensitycategory',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energydensitycategory',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energyeffectivenessratiocategory',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energyeffectivenessratiocategory',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
