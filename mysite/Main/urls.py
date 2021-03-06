from django.conf.urls import url

from .views import(
    #Main Views
    HomeView,
    post_create,
    post_detail,
    edit_post,
    post_deleteview,
    all_properties,
    ##
    #PostCreateView,
     ### Gallery Urls
     gallery_list,
     gallery_createview,
     gallery_detail,
     edit_gallery_post,
     gallery_deleteview,
     test,
     contact

     #GalleryListView,
 
     
 )








urlpatterns = [
    url(r'^$',HomeView,name='home-view'),
    url(r'^test/$',test,name='test'),

    url(r'^contact/$',contact,name='contact'),

    url(r'^our-properties/$',all_properties,name='all_properties'),

    url(r'^(?P<id>\d+)/edit-gallery/$',edit_gallery_post,name='edit_gallery_post'),
   # url(r'^create/$',PostCreateView.as_view(),name='create'),
    url(r'^post_create/$',post_create,name="post_create" ),
    url(r'^(?P<slug>[\w-]+)/delete/$',post_deleteview,name='delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$',edit_post,name='edit_post'),
    

    #Galery
    url(r'^gallery_list/$',gallery_list,name="gallery_list" ),
    url(r'^gallery_create/$',gallery_createview,name="gallery_create" ),
    url(r'^(?P<id>\d+)/$',gallery_detail,name='gallery_detail'),
    url(r'^(?P<id>\d+)/gallery_deleteview/$',gallery_deleteview,name='gallery_deleteview'),
    


    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
]