# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Post
# Create your views here.



class PostListView(ListView):
    pass




class PostDetailView(DetailView):
    pass


class PostCreateView(CreateView):
    pass



class PostUpdateView(UpdateView):
    pass


class PostDeleteView(DeleteView):
    pass


