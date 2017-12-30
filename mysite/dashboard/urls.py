from django.conf.urls import url


from .views import *







urlpatterns = [
    url(r'^$',Dashboard,name="dashboard" ), 
    url(r'^dash_base$',dash_base,name="dash_base" ),
    url(r'^bich/$',DashboardPostListView.as_view(),name="dashboard-listing" ),

    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]