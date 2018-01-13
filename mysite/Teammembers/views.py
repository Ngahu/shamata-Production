# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,get_object_or_404,redirect
from .models import Team_Meamber
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import Team_MeamberForm
from django.http import Http404 ,HttpResponseRedirect


def team_list(request):
    """
    This View returns alist of all the teammembers in the database
    """
    queryset = Team_Meamber.objects.all()
    context = {
       "member_list":queryset,
       "title":"List all members here "
    }
    template_name = 'Teammembers/team_list.html'
    return render(request, template_name, context)




def team_list_main_site(request):
    """
    This view is responsible to return a queryset paginated with only three team members  For the main Website 
    """
    members_list = Team_Meamber.objects.all()
    paginator = Paginator(members_list,5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
       "team_list":queryset,
       "title":"List Page for main website"
    }
    template_name = 'Teammembers/team_mainsite.html'
    return render(request, template_name, context)






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
        return HttpResponseRedirect(instance.get_absolute_url_2())
    context = {
        "form": form,
        "title": "Create Member Listing",
    }
    template_name = 'dashboard/teammember_create.html'
    #template = 'property-create.html'
    return render(request, template_name, context)



def team_member_detailview(request,id=None):
    instance = get_object_or_404(Team_Meamber,id=id)
    context = {
        "instance": instance
    }
    template_name = 'dashboard/teammember_detail.html'
    return render(request, template_name, context)

      

def team_member_updateview(request,id=None):
    #make sure that the one that is editing the post is an admin or super user
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    post =get_object_or_404(Team_Meamber,id=id)
    if request.method == "POST":
        form = Team_MeamberForm(request.POST , request.FILES,instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url_2())

    else:
        form = Team_MeamberForm(instance=post)
    template_name = 'dashboard/teammember_create.html'
    context = {
        'form':form
    }
    return render(request, template_name, context)



def team_member_deleteview(request,id=None):
    instance = get_object_or_404(Team_Meamber,id=id)
    instance.delete()
    return redirect("Teammembers:list")




