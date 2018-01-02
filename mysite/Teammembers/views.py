# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Team_Meamber
# Create your views here.
from .forms import Team_MeamberForm

class Team_MeamberListView(ListView):
    queryset = Team_Meamber.objects.all()



class Team_MeamberCreateView(CreateView):
    form_class = Team_MeamberForm
    template_name = 'dashboard/team_member_create.html'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(Team_MeamberCreateView,self).form_valid(form)

        
        



class Team_MeamberUpdateView(UpdateView):
    pass


class Team_MeamberDetailView(DetailView):
    queryset = Team_Meamber.objects.all()


class Team_MeamberDeleteView(DeleteView):
    pass
