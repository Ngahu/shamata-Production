from django.conf.urls import url


from .views import *







urlpatterns = [
    url(r'^$',Dashboard,name="dashboard" ),
    url(r'^bich/$',DashboardPostListView.as_view(),name="dashboard-listing" ),

    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]