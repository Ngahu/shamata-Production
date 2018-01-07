# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Gallery(models.Model):
    image_title        =  models.CharField(max_length=100)
    image_description  =  models.TextField()
    gallery_image      =  models.ImageField(upload_to=upload_location,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.image_title

    def __unicode__(self):
        return self.image_title


    def get_gallery_absolute_url(self):
        return reverse("Main:gallery_detail",kwargs={"id":self.id})


    def get_gallery_edit_absolute_url(self):
        return reverse("Main:edit_gallery_post",kwargs={"id":self.id})


    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Gallery"