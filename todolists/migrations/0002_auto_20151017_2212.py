# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='task_ref',
            field=models.ForeignKey(related_name='comments', to='todolists.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='todo_list_ref',
            field=models.ForeignKey(related_name='tasks', to='todolists.TODOList'),
        ),
    ]
