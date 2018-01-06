from django.conf.urls import urls

from .views import (
    comment_delete
)

urlpatterns = [
    url(r'^(?P<id>\d+)delete/$',comment_delete,),
]