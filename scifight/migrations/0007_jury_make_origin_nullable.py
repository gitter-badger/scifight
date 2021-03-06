# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scifight', '0006_fightstage_remove_many_to_many'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fight',
            name='juries',
            field=models.ManyToManyField(blank=True, to='scifight.Jury'),
        ),
        migrations.AlterField(
            model_name='jury',
            name='origin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scifight.CommonOrigin'),
        ),
    ]
