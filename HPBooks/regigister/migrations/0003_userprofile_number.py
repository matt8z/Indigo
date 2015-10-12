# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regigister', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
