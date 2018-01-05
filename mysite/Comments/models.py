# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL 



class CommentManager(models.Manager):
    def filter_by_instance(self,instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)# instance.__class__ a way to get python's class
        obj_id = instance.id
        qs = super(CommentManager,self).filter(content_type=content_type,object_id=obj_id)
        return qs 



class Comment(models.Model):
    owner      = models.ForeignKey(User, on_delete=models.CASCADE)


    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self",blank=True, null=True)
    content   =  models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return str(self.owner.username)

    def __str__(self):
        return str(self.owner.username)

    #get replies 
    def children(self):
        return Comment.objects.filter(parent=self)


    @property
    def is_parent(Self):
        if self.parent is not None:
            return False
        return True