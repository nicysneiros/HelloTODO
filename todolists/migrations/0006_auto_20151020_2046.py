# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0005_todolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(related_name='todolists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
