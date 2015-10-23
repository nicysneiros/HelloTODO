# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0002_auto_20151017_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='task_ref',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='todo_list_ref',
            new_name='todolist',
        ),
    ]
