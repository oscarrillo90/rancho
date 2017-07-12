# main_app/urls.py
from django.conf.urls import url
from views import index, menu, about, gallery, home, appetizers, soupSalad, texmex, entrees, mexican, kids, lunch


urlpatterns = [
    url(r'^$', index),
    url(r'^home/$', home, name="home"),
    url(r'^menu/$', menu, name="menu"),
    url(r'^about/$', about, name="about"),
    url(r'^gallery/$', gallery, name="gallery"),
    url(r'^appetizers/$', appetizers, name="appetizers"),
    url(r'^soupSalad/$', soupSalad, name="soupSalad"),
    url(r'^texmex/$', texmex, name="texmex"),
    url(r'^entrees/$', entrees, name="entrees"),
    url(r'^mexican/$', mexican, name="mexican"),
    url(r'^kids/$', kids, name="kids"),
    url(r'^lunch/$', lunch, name="lunch"),

]
