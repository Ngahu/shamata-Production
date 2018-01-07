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
     gallery_detail,
     edit_gallery_post,

     #GalleryListView,
 
     
 )








urlpatterns = [
    url(r'^(?P<id>\d+)/edit-gallery/$',edit_gallery_post,name='edit_gallery_post'),
    url(r'^$',PostListView.as_view(),name='list'),
    url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^post_create/',post_create,name="post_create" ),
    url(r'^(?P<slug>[\w-]+)/delete/$',post_deleteview,name='delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$',edit_post,name='edit_post'),
    

    #Galery
    url(r'^gallery_create/',gallery_createview,name="gallery_create" ),
    url(r'^(?P<id>\d+)/$',gallery_detail,name='gallery_detail'),
    


    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
]