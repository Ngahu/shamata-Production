# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL 



def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)



class Post(models.Model):
    owner =  models.ForeignKeyField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_location)
    image_2 = models.ImageField(upload_to=upload_location)
    image_3 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    image_4 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    image_5 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    description = models.TextField()
    size_of_land = models.models.CharField(max_length=150)
    location_details = models.CharField(max_length=300)
    price = models.models.CharField(max_length=150)
    features = models.models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        pass
        #return reverse("Main:detail",kwargs={"slug":self.slug})
    class Meta:
        ordering = ["-timestamp", "-updated"]




