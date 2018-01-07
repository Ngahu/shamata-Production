from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^dashboard/',include('dashboard.urls', namespace='dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^newsletter/',include('newsletter.urls', namespace='newsletter')),
    url(r'^team/',include('Teammembers.urls', namespace='Teammembers')),
    url(r'^',include('Main.urls', namespace='Main')),
    

    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)