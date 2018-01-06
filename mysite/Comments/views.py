# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import  CommentForm
from .models import Comment

def  comment_delete(request,id):
    obj = get_object_or_404(Comment,id=id)
    context = {
        "object":obj
    }
    template_name = 'Main/confirm_delete.html'
    return render(request,template_name,context)
