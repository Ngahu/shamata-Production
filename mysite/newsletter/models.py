# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Subscribe(models.Model):
    name =models.CharField(max_length=50)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Newsletter Subscriptions"

    def __unicode__(self):
        return self.email

    def get_delete_url(self):
        return reverse("newsletter:my_email_list",kwargs={"id": self.id})
