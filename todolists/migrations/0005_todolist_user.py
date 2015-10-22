# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0004_auto_20151020_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(related_name='todolists', default=1, to='todolists.User'),
            preserve_default=False,
        ),
    ]
