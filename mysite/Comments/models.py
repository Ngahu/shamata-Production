# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL 

from Main.models import Post
# Create your models here.

class Comment(models.Model):
    owner      = models.ForeignKey(User, on_delete=models.CASCADE)
    post      = models.ForeignKey(Post)
    content   =  models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return str(self.owner.username)

    def __str__(self):
        return str(self.owner.username)
    