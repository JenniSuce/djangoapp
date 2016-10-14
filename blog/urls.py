from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.listar_articulo),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.postear_nuevo, name='postear_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_articulo, name='editar_articulo'),
]
