# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now
 
from theinkspot.users.models import User
 
 
class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(_("Title"), max_length=100)
    description = models.CharField(_("Description"), null=True, max_length=500)
    public = models.BooleanField(_("Public"), default=True)
    created = models.DateTimeField(_("Created at"), auto_now_add=True)
    edited = models.DateTimeField(_("Last Edit"), auto_now_add=True)
 
    def __str__(self):
        return self.title
