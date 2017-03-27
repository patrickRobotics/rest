"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^farmers/$', views.users_list),
    url(r'^farmers/(?P<pk>[0-9]+)/$', views.farmers_detail),
]
"""

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^farmers/$', views.FarmersList.as_view()),
    url(r'^farmers/(?P<pk>[0-9]+)/$', views.FarmersDetail.as_view()),
    url(r'^locations/$', views.LocationsList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
