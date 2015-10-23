# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=500)),
                ('deadline', models.DateTimeField()),
                ('done', models.BooleanField(default=False)),
                ('order_list', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TODOList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='todo_list_ref',
            field=models.ForeignKey(to='todolists.TODOList'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task_ref',
            field=models.ForeignKey(to='todolists.Task'),
        ),
    ]
