from django.conf.urls import url


from .views import *







urlpatterns = [
    ##dash_board/
    url(r'^$',dash_board,name="dash_board" ),
    url(r'^dash_board_help/$',dash_board_help,name="dash_board_help" ),


    #url(r'^$',Dashboard,name="dashboard" ), 
    url(r'^dash_base$',dash_base,name="dash_base" ),
    url(r'^bich/$',DashboardPostListView.as_view(),name="dashboard-listing" ),
    url(r'^team-listing/$',DashboardTeam_MembersListView.as_view(),name="team-listing" ),






    
    #url(r'^restaurants/(?P<slug>[\w-]+)/$',RestaurantListView.as_view()),
    #url(r'^',restaurant_listview,name="list" ),
]

