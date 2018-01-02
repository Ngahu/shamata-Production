from django.conf.urls import url

from .views import (
    Team_MeamberListView,
    Team_MeamberCreateView,
    Team_MeamberDetailView

)



urlpatterns = [  
    url(r'^list/$',Team_MeamberListView.as_view(),name='list'),
    url(r'^create/$', Team_MeamberCreateView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/$',Team_MeamberDetailView.as_view(),name='detail'),
    #url(r'^post_create/',post_create,name="post_create" ),
    #url(r'^(?P<slug>[\w-]+)/$',PostDetailView.as_view(),name='detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
