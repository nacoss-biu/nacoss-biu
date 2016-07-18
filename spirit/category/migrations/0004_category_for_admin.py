# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_category', '0003_category_is_global'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='for_admin',
            field=models.BooleanField(default=False, verbose_name='admin'),
        ),
    ]
