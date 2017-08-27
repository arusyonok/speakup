# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('steps', '0005_auto_20170827_1925'),
        ('users', '0005_userexercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='steps.Step')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='userexercise',
            name='exercise_id',
        ),
        migrations.RemoveField(
            model_name='userexercise',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='UserExercise',
        ),
    ]
