# main_app/urls.py
from django.conf.urls import url
from views import index, menu, about, gallery, home, appetizers


urlpatterns = [
    url(r'^$', index),
    url(r'^home/$', home, name="home"),
    url(r'^menu/$', menu, name="menu"),
    url(r'^about/$', about, name="about"),
    url(r'^gallery/$', gallery, name="gallery"),
    url(r'^appetizers/$', appetizers, name="appetizers"),


]
