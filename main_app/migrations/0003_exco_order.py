# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20160222_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='exco',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
    ]
