# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.



class PostListView(ListView):
    queryset = Post.objects.all()




class PostDetailView(DetailView):
    pass


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'Main/post_create.html'


    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(PostCreateView,self).form_valid(form)



class PostUpdateView(UpdateView):
    pass


class PostDeleteView(DeleteView):
    pass


