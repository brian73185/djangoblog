from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^update/(?P<id>[0-9])/$', views.article_update, name='update'),
    url(r'^delete/(?P<id>[0-9])/$', views.confirm_delete, name='delete'),
    # url(r'^author/(?P<author_id>[0-9])/$', views.author_list, name='author'),
    url(r'^(?P<id>[0-9])/$', views.article_detail, name="details"),
]
