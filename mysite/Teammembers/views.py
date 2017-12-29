# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Team_Meamber
# Create your views here.


class Team_MeamberListView(ListView):
    pass



class Team_MeamberCreateView(CreateView):
    pass


class Team_MeamberListView(ListView):
    pass


class Team_MeamberUpdateView(UpdateView):
    pass


class Team_MeamberDetailView(DetailView):
    pass


class Team_MeamberDeleteView(DeleteView):
    pass
