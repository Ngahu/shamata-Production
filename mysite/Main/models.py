# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

# Create your models here.

User = settings.AUTH_USER_MODEL 

from Comments.models import Comment


def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)



class Post(models.Model):
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug      =      models.SlugField(unique=True,blank=True, null=True)
    image = models.ImageField(upload_to=upload_location)
    image_2 = models.ImageField(upload_to=upload_location)
    image_3 = models.ImageField(upload_to=upload_location,blank=True, null=True)
    description = models.TextField()
    size_of_land = models.CharField(max_length=150)
    location_details = models.CharField(max_length=300)
    price = models.CharField(max_length=150)
    features = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.title


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("Main:post_detail",kwargs={"slug":self.slug})

    def get_edit_url(self):
        return reverse("Main:edit_post",kwargs={"slug":self.slug})

    def get_delete_url(self):
        return reverse("Main:delete", kwargs={"slug":self.slug})


    class Meta:
        ordering = ["-timestamp", "-updated"]
    

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type




def Post_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



pre_save.connect(Post_pre_save_receiver,sender=Post)




#for the Gallery

class Gallery(models.Model):
    image_title        =  models.CharField(max_length=100)
    image_description  =  models.TextField(blank=True, null=True)
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

    def get_gallery_delete_absolute_url(self):
        return reverse("Main:gallery_deleteview",kwargs={"id":self.id})


    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Gallery"