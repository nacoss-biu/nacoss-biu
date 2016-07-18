# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20160222_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
    ]
