# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Subscribe,Testimony
from .forms import SubscriptionForm,TestimonyForm
from django.views.generic import  FormView, CreateView,ListView
from .models import Subscribe
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

#This view will be displaying a list of the emails that have subscribed to the news letter section 
def my_email_list(request):
    queryset = Subscribe.objects.all()
    context = {
        "queryset":queryset
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







class  TestimonyCreateView(LoginRequiredMixin,CreateView):
    template_name = 'testimony/create.html'
    form_class = TestimonyForm
    success_url = '/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(TestimonyCreateView,self).form_valid(form)




#Return back a List of all the Testimonies in the database Regaldress of the owner
class TestimonyListView(ListView):
    template_name = 'testimony/testimony_list.html'
    queryset = Testimony.objects.all()



class TestimonyDetailView():
    pass
