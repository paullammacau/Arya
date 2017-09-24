# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_activitylog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='lastupate_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]