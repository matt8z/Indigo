# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regigister', '0003_userprofile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='number',
            field=models.CharField(max_length=12),
        ),
    ]
