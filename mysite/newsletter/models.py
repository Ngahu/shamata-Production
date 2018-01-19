# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL 

from django.core.urlresolvers import reverse

def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Subscribe(models.Model):
    name = models.CharField(max_length=100)
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
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    testimony = models.TextField()
    image = models.ImageField(upload_to=upload_location,blank=True, null=True)
    approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Testimonies"


    def __unicode__(self):
        return str(self.owner)

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('newsletter:testimony_detail', kwargs={'pk': self.pk})
