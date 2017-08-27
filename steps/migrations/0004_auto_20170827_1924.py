# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0003_auto_20170827_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='step_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steps.Step'),
        ),
    ]