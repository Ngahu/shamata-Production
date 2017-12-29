# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
# phone number
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)


class Team_Meamber(models.Model):
    members_name = models.CharField(max_length=100)
    members_role = models.CharField(max_length=100)
    #slug = models.SlugField(unique=True)
    members_details = models.TextField()
    members_phone_number = PhoneNumberField(blank=True, null=True)
    members_email = models.EmailField()
    members_image = models.ImageField(upload_to=upload_location) #null=False,blank=False
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.members_name


    def __unicode__(self):
        return self.members_name


    # def get_absolute_url(self):
    #     return reverse("Teammembers:detail",kwargs={"slug":self.slug})

    def get_absolute_url(self):
        return reverse("Teammembers:detail",kwargs={"id": self.id})






# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Team_Meamber.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)



# pre_save.connect(pre_save_post_receiver, sender=Team_Meamber)