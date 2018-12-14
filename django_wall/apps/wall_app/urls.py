from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^welcome$', views.welcome),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^show$', views.show),
    url(r'^delete$', views.delete),
    #--------wall section here
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete_post/(?P<my_val>\d+)$', views.delete_post),
]