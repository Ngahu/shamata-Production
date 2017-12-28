from django.conf.urls import url

from .views import(
     PostCreateView,
     PostDetailView,
     PostDeleteView,
     PostListView,
     PostUpdateView
     
 )








urlpatterns = [
    url(r'^$',PostListView.as_view(),name='list'),
    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]