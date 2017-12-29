from django.conf.urls import url

from .views import (
    Team_MeamberListView

)



urlpatterns = [  
    url(r'^list/$',Team_MeamberListView.as_view(),name='list'),
    #url(r'^create/$',PostCreateView.as_view(),name='create'),
    #url(r'^post_create/',post_create,name="post_create" ),
    #url(r'^(?P<slug>[\w-]+)/$',PostDetailView.as_view(),name='detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]
