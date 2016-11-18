#from django.contrib import admin
#from .models import Postear
#admin.site.register(Postear)
#recuerde que es necesario indicar que clases de nuestro modelo van a ser manejadas por la aplicación /admin.

from django.contrib import admin
from .models import Alumnos, AlumnosAdmin, Cursos, CursosAdmin

#Registramos nuestras clases principales.
admin.site.register(Cursos, CursosAdmin)
admin.site.register(Alumnos, AlumnosAdmin)
