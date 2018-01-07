# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Subscribe
from .forms import SubscriptionForm
from django.views.generic import  FormView
from .models import Subscribe

#This view will be displaying a list of the emails that have subscribed to the news letter section 

def my_email_list(request):
    queryset = Subscribe.objects.all()
    context = {
        "queryset":queryset
    }
    template_name = 'newsletter/newsletter_list.html'
    return render(request, template_name, context)



class SubscribeView(FormView):
    template_name = 'newsletter/subscribe.html'
    form_class = SubscriptionForm