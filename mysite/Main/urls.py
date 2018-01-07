from django.conf.urls import url

from .views import(
    #Main Views
    post_create,
    post_detail,
    edit_post,
    post_deleteview,
    ##
     PostCreateView,
     PostListView,
     ### Gallery Urls
     gallery_createview,

     GalleryListView,
 
     
 )








urlpatterns = [
    url(r'^$',PostListView.as_view(),name='list'),
    url(r'^gallery/$',GalleryListView.as_view(),name='gallery'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^post_create/',post_create,name="post_create" ),
    url(r'^gallery_create/',gallery_createview,name="gallery_create" ),

    url(r'^(?P<slug>[\w-]+)/delete/$',post_deleteview,name='delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$',edit_post,name='edit_post'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]