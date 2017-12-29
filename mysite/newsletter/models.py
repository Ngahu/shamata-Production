# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Newsletter Subscriptions"

    def __unicode__(self):
        return self.email
