__author__ = 'kt'
from django.conf.urls import *
from blog.views import blogView, articleView, searchView, friendsView


urlpatterns = [
    url(r'^$', blogView),
    url(r'^archives/', articleView),
    url(r'^search/', searchView),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^friends/', friendsView),


]