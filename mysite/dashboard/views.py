# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
#from Main.views import
from Main.models import Post
from Teammembers.models import Team_Meamber

##The Dashboard Views From Here

def Dashboard(request):# incharge of the secong dmin panell for editing the website
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
         "title":"Welcome to the  Dashboard",
         "title_small":" Admin Overview"
    }
    return render(request,"dashboard/dashboard.html",context)


## Delete from here 

class DashboardPostListView(LoginRequiredMixin,ListView):
    template_name = 'Dashboard/listings.html'
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)




class DashboardTeam_MembersListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/team-listing.html'
    def get_queryset(self):
        return Team_Meamber.objects.all()



## Delete to here 



def dash_base(request):
    context = {}
    template_name = 'dashboard/team-listing.html'#base_dash.html
    return render(request,template_name,context)



