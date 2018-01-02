# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from .models import Team_Meamber
# Create your views here.
from .forms import Team_MeamberForm
from django.http import Http404 ,HttpResponseRedirect



class Team_MeamberListView(ListView):
    queryset = Team_Meamber.objects.all()





def team_member_createview(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = Team_MeamberForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        # message success
        #messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Create Member Listing",
    }
    template_name = 'dashboard/teammember_create.html'
    #template = 'property-create.html'
    return render(request, template_name, context)











# def team_member_createview(request):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#         form = team_memberForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             instance = form,save(commit=False)
#             instance.owner = request.owner
#             instance.save()
#             return HttpResponseRedirect(instance.get_absolute_url())
#         context = {
#             "form" :form,
#             "title": "Create Member Listing",
#         }
#         template_name = 'dashboard/teammember_create.html'
#         return render(request, template_name, context)




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
