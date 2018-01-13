# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Subscribe
from .forms import SubscriptionForm
from django.views.generic import  FormView, CreateView,DetailView,DeleteView
from .models import Subscribe
from Comments.models import Comment
from django.contrib.messages.views import SuccessMessageMixin

#This view will be displaying a list of the emails that have subscribed to the news letter section 

def my_email_list(request):
    queryset = Subscribe.objects.all()
    comment_count = Comment.objects.count()
    context = {
        "comment_count":comment_count,
        "email_list":queryset
    }
    template_name = 'newsletter/newsletter_list.html'
    return render(request, template_name, context)



class SubscribeView(SuccessMessageMixin,CreateView):
    template_name = 'newsletter/subscribe.html'
    form_class = SubscriptionForm
    success_url = '/'

    def get_success_message(self,cleaned_data):
        #see what the cleaned_data is
        print(cleaned_data)

    # def form_valid(self,form):
    #     email = form.cleaned_data.get("email")
    #     #can do other things here like sending an email 
    #     return super(SubscribeView,self).form_valid(form)



def newsletter_detail(request,id=None):
    instance = get_object_or_404(Subscribe,id=id)
    context = {
        "instance":instance
    }
    template_name = 'newsletter/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                '
    return render(request,template_name, context)




def deleteview(request):
    instance = get_object_or_404(Subscribe,id=id)
    instance.delete()
    return redirect("newsletter:my_email_list")












####THe testimonies Views 

class SubmitTestimonyView(CreateView):
    pass



class TestimonyDetailView(DetailView):
    pass


class TestimonyDeleteView(DeleteView):
    pass
    


