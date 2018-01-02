from django.conf.urls import url

from .views import (
    Team_MeamberListView,
    Team_MeamberCreateView,
    Team_MeamberDetailView,
    team_member_createview

)



urlpatterns = [  
    url(r'^list/$',Team_MeamberListView.as_view(),name='list'),
    url(r'^create/$', Team_MeamberCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',Team_MeamberDetailView.as_view(),name='detail'),
    url(r'^team_member_create/',team_member_createview,name="team_member_create" ),
    #url(r'^(?P<slug>[\w-]+)/$',PostDetailView.as_view(),name='detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
