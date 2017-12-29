# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView,CreateView
from django.shortcuts import render
from .models import Subscribe
from .forms import SubscriptionForm
# Create your views here.


#This view will be displaying a list of the emails that have subscribed to the news letter section 
class SubscriptionsListView(ListView):
    pass




class SubscriptionsListView(ListView):
    pass



class SubscriptionsCreateView(CreateView):
    pass

