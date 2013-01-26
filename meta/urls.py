from django.conf.urls import patterns, url, include
from meta.api import v1

from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(v1.urls))
)
