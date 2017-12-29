# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Post,Gallery
from .forms import PostForm

from django.http import Http404
# Create your views here.



class PostListView(ListView):
    queryset = Post.objects.all()



class PostDetailView(DetailView):
    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'Main/post_create.html'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(PostCreateView,self).form_valid(form)



 

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        # message success
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Create Property Listing",
    }
    template_name = 'Main/post_create.html'
    #template = 'property-create.html'
    return render(request, template_name, context)







class PostUpdateView(UpdateView):
    pass


class PostDeleteView(DeleteView):
    pass







###The Gallery Views from here 

class GalleryCreateView(CreateView):
    pass


class GalleryListView(ListView):
    queryset = Gallery.objects.all()


class GalleryUpdateView(UpdateView):
    pass


class GalleryDeleteView(DetailView):
    pass




