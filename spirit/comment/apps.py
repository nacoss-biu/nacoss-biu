# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig

from django.contrib import admin
# from . import models

class SpiritCommentConfig(AppConfig):

    name = 'spirit.comment'
    verbose_name = "Spirit Comment"
    label = 'spirit_comment'

# admin.site.register(models.Comment)