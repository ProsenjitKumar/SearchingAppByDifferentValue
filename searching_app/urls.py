from django.conf.urls import re_path
from .views import ActorsSearchList


urlpatterns = [
    re_path('^$', ActorsSearchList.as_view(), name='search_list'),
]