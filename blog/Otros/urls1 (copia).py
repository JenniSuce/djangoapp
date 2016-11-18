#from django.conf.urls import include, url
#from . import views
from django.conf.urls import url
from . import views

#urlpatterns = [
#    url(r'^$', views.listar_articulo),
#    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
#    url(r'^post/new/$', views.postear_nuevo, name='postear_nuevo'),
#    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar_articulo, name='editar_articulo'),
#]
#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [
    url(r'^$', views.listar_alumnos),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.alumno_nuevo, name='alumno_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.alumno_editar, name='alumno_editar'),
]
