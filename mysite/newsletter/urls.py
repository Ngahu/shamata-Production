from django.conf.urls import url

from .views import (
    my_email_list,
    SubscribeView,
    deleteview,
    
)

urlpatterns = [ 
    url(r'^my_email_list/$',my_email_list,name='my_email_list'),
    url(r'^subscribe/$',SubscribeView.as_view(),name='subscribe'),

    url(r'^(?P<id>\d+)/deleteview/$',deleteview,name='deleteview'),
]
