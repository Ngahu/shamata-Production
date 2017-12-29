from django.conf.urls import url

from .views import(
     PostCreateView,
     PostDetailView,
     PostDeleteView,
     PostListView,
     PostUpdateView,
     post_create,
     ### Gallery Urls
     GalleryListView,
     ##Dashboard
     Dashboard,
     DashboardPostListView
     
 )








urlpatterns = [
    url(r'^bich/$',DashboardPostListView.as_view(),name="dashboard-listing" ),
    # url(r'^$',PostListView.as_view(),name='list'),
    # url(r'^gallery/$',GalleryListView.as_view(),name='gallery'),
    # url(r'^dashboard/$',Dashboard,name="dashboard" ),
    # url(r'^create/$',PostCreateView.as_view(),name='create'),
    # url(r'^post_create/',post_create,name="post_create" ),
    # url(r'^(?P<slug>[\w-]+)/$',PostDetailView.as_view(),name='detail'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]