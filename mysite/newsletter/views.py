# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Subscribe
from .forms import SubscriptionForm
from django.views.generic import  FormView, CreateView
from .models import Subscribe

#This view will be displaying a list of the emails that have subscribed to the news letter section 

def my_email_list(request):
    queryset = Subscribe.objects.all()
    context = {
        "queryset":queryset
    }
    template_name = 'newsletter/newsletter_list.html'
    return render(request, template_name, context)



class SubscribeView(CreateView):
    template_name = 'newsletter/subscribe.html'
    form_class = SubscriptionForm
    success_url = '/'

    def form_valid(self,form):
        email = form.cleaned_data.get("email")
        #can do other things here like sending an email 
        return super(SubscribeView,self).form_valid(form)
    