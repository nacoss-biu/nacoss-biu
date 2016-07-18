# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_exco_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('position', models.CharField(max_length=30, verbose_name='position')),
            ],
        ),
        migrations.AlterField(
            model_name='exco',
            name='bio',
            field=models.TextField(verbose_name='bio', blank=True),
        ),
        migrations.AlterField(
            model_name='exco',
            name='contact',
            field=models.CharField(max_length=30, verbose_name='contact', blank=True),
        ),
    ]
