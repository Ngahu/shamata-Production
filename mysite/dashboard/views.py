# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
#from Main.views import
from Main.models import Post


##The Dashboard Views From Here

def Dashboard(request):# incharge of the secong dmin panell for editing the website
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    context = {
         "title":"Welcome to the  Dashboard",
         "title_small":" Admin Overview"
    }
    return render(request,"dashboard/dashboard.html",context)


class DashboardPostListView(LoginRequiredMixin,ListView):
    template_name = 'Dashboard/listings.html'
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)



class DashboardTeam_MembersListView(ListView):
    pass
    






def dash_base(request):
    context = {}
    template_name = 'dashboard/base_dash.html'
    return render(request,template_name,context)