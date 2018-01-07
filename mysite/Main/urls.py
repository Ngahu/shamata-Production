from django.conf.urls import url

from .views import(
     PostCreateView,
     PostListView,
     post_create,
     ### Gallery Urls
     GalleryListView,
     post_update,
     edit_post,
     post_detail
 
     
 )








urlpatterns = [
    url(r'^$',PostListView.as_view(),name='list'),
    url(r'^gallery/$',GalleryListView.as_view(),name='gallery'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^post_create/',post_create,name="post_create" ),
    #url(r'^(?P<slug>[\w-]+)/$',PostDetailView.as_view(),name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$',post_update,name='post_update')
    url(r'^(?P<slug>[\w-]+)/edit/$',edit_post,name='edit_post'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]