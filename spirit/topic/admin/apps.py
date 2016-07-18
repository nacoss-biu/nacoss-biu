# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
from django.contrib import admin
from .. import models


class SpiritTopicAdminConfig(AppConfig):

    name = 'spirit.topic.admin'
    verbose_name = "Spirit Topic Admin"
    label = 'spirit_topic_admin'

admin.site.register(models.Topic)