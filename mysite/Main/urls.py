from django.conf.urls import url

from .views import(
     PostCreateView,
     PostDetailView,
     PostDeleteView,
     PostListView,
     PostUpdateView,
     post_create
     
 )








urlpatterns = [
    url(r'^$',PostListView.as_view(),name='list'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^post_create/',post_create,name="post_create" ),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]