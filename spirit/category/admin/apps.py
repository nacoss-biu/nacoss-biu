# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig

from django.contrib import admin
from .. import models

class SpiritCategoryAdminConfig(AppConfig):

    name = 'spirit.category.admin'
    verbose_name = "Spirit Category Admin"
    label = 'spirit_category_admin'

admin.site.register(models.Category)