# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spirit_category', '0004_category_for_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='for_admin',
            new_name='admin',
        ),
    ]
