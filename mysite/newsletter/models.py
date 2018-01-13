# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


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






class Testimony(models.Model):
    owner      = models.ForeignKey(User, on_delete=models.CASCADE)
    subject    = models.CharField(max_length=100)
    testimony  = models.TextField()
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return str(self.owner)

    class  Meta:
        ordering = ["-timestamp"]
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonies"