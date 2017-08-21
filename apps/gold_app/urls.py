from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^play$', views.play),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
    url(r'^(?P<user_id>\d+)/showplayer$', views.showplayer),
    url(r'^logout$', views.logout),
]