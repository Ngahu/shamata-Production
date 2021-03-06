# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Gallery
from .forms import PostForm,GalleryForm,ContactForm
from django.http import Http404 ,HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from Comments.models import Comment
from Comments.forms import CommentForm
from Teammembers.models import Team_Meamber
from django.conf import settings
from django.core.mail import send_mail


def contact(request):
    form = ContactForm(request.POST or None)
    title = 'Drop Us A Line'
    confirm_message = None
   
    if form.is_valid():
        print request.POST
        print form.cleaned_data['email']

        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message  From Shamata Website'
        message = '%s %s' %(comment,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_EMAIL]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=False,)

        #after the email is successfully sent by the user 
        title = "Message Sent!"
        confirm_message = "Thankyou for your message .We will get back to you as soon as we can!."
        form = None

    context = {
        "title":title,
        "form":form,
        "confirm_message":confirm_message
    }
    template_name = 'Main/contact.html'
    return render(request,template_name,context)



#this is for the testing detail page
def test(request):
    context = {
        "Title":"title"
    }
    template_name = 'Main/test.html'
    return render(request, template_name, context)




def HomeView(request):
    """"
    This is the home View.Its the Entry Point of the project.This will render the homepage.
    """
    qs = Post.objects.all()[:6] #limiting the queryset to only 6 posts
    agent_list = Team_Meamber.objects.all()[:4]#Filtering only four teammembers
    context = {
        "agents_list":agent_list,
        "post_list":qs,
        "title":"title is here"
    }
    template_name = 'Main/index.html'
    return render(request, template_name, context)



def all_properties(request):
    queryset = Post.objects.all()
    context = {
        "all_properties":queryset
    }
    template_name = 'Main/all_properties.html'
    return render(request, template_name, context)

# class PostCreateView(CreateView):
#     form_class = PostForm
#     template_name = 'Main/post_create.html' #TODO This should be moved to the dashboard app forthe templates for easy management of the project 

#     def form_valid(self,form):
#         instance = form.save(commit=False)
#         instance.owner = self.request.user
#         return super(PostCreateView,self).form_valid(form)




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



def post_detail(request,slug=None):#   showing details
    instance = get_object_or_404(Post, slug=slug)

    initial_data = {
        "content_type":instance.get_content_type,
        "object_id":instance.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        #print(form.cleaned_data)
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id")) #Get the  Parent_id
        except:
            parent_id = None
        
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id) #Check if the parent_id exists in the database
            if parent_qs.exists() and  parent_qs.count() ==1 :
                parent_obj = parent_qs.first()


        new_comment, created =  Comment.objects.get_or_create(
                                owner = request.user,
                                content_type = content_type,
                                object_id = obj_id,
                                content = content_data,
                                parent = parent_obj,
                                )        
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    comments = instance.comments#Comment.objects.filter_by_instance(instance) 
    context = {
        "instance": instance,
        "comments":comments,
        "comment_form":form,
    }
    template_name = 'Main/detail.html'
    return render(request,template_name, context)


def edit_post(request,slug):
    #make sure that the one that is editing the post is an admin or super user
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    post =get_object_or_404(Post,slug=slug)
    if request.method == "POST": 
        form = PostForm(request.POST , request.FILES,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            #post = form.save(commit=False)
            instance.owner = request.user
            #post.owner = request.user
            instance.save()
            #post.save()
            return HttpResponseRedirect(instance.get_absolute_url())
            #return redirect('Main:list')
    else:
        form = PostForm(instance=post)
    template_name = 'Main/post_create.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)
            

def post_deleteview(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    return redirect("Main:list")



###The Gallery Views from here 

def gallery(request):
    queryset = Gallery.objects.all()
    context = {
        "gallery_all":queryset
    }
    template_name = 'gallery/gallery.html'
    return render(request, template_name, context)






def gallery_list(request):
    queryset = Gallery.objects.all()
    context = {
        "gallery_list":queryset,
        "title":"this is the gallery listview"
    }
    template_name = 'gallery/gallery_list.html'
    return render(request, template_name, context)


def gallery_createview(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = GalleryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save(commit=False) 
        instance.owner = request.user  
        instance.save()  

        return HttpResponseRedirect(instance.get_gallery_absolute_url())   
    context = {
        "form":form,
        "title":"Gallery Create Form"
    }
    template_name = 'gallery/gallery_create.html'

    return render(request, template_name, context)


def gallery_detail(request,id=None):
    instance = get_object_or_404(Gallery,id=id)
    context = {
        "instance":instance
    }
    template_name = 'gallery/gallery_detail.html'
    return render(request,template_name, context)



def edit_gallery_post(request,id=None):
    #make sure that the one that is editing the post is an admin or super user
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    post =get_object_or_404(Gallery,id=id)
    if request.method == "POST": 
        form = GalleryForm(request.POST , request.FILES,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect(instance.get_gallery_absolute_url())
            
    else:
        form = GalleryForm(instance=post)
    template_name = 'gallery/gallery_create.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)


def gallery_deleteview(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    return redirect("Main:gallery_list")






