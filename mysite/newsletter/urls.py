from django.conf.urls import url

from .views import (
    my_email_list
)

urlpatterns = [ 
     url(r'^my_email_list/$',my_email_list,name='my_email_list'),
]