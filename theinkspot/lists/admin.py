# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from theinkspot.lists.models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "description", "private", "created", "modified"]
