# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 02:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20170917_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.Project')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kanban.Stage'),
        ),
        migrations.AlterUniqueTogether(
            name='stage',
            unique_together=set([('project', 'title')]),
        ),
    ]
