from django.conf.urls import url

from .views import (
    team_member_createview,
    team_member_detailview,
    team_member_updateview,
    team_member_deleteview,
    team_list_main_site,
    agents_list

)

urlpatterns = [ 

    url(r'^agents_list/$',agents_list,name="agents_list" ),



    url(r'^team_member_create/$',team_member_createview,name="team_member_create" ),

    url(r'^team_list_main_site/$',team_list_main_site,name="main-list" ),
    url(r'^(?P<id>\d+)/edit/$',team_member_updateview,name='edit'),
    url(r'^(?P<id>\d+)/delete/$',team_member_deleteview,name='delete'),
    url(r'^(?P<id>\d+)/$',team_member_detailview,name='detail'),
    
]
