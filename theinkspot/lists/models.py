# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from theinkspot.users.models import User


class List(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=100)
    description = models.CharField(_("Description"), null=True, max_length=500)
    private = models.BooleanField(_("Private"), default=True)

    def __str__(self):
        return self.title
