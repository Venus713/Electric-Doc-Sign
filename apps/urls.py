from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
    url('auth/', include('apps.authentication.urls')),
]