#from django.db import models
#from django.utils import timezone
from django.db import models
from django.contrib import admin

#class Postear(models.Model):
#    autor = models.ForeignKey('auth.User')
#    titulo = models.CharField(max_length=200)
#    texto = models.TextField()
#    creacion_date = models.DateTimeField(
#                    default=timezone.now)
#    publicacion_date = models.DateTimeField(
#                        blank=True, null=True)

#    def publicar(self):
#        self.publicacion_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.titulo



class Persona(models.Model):
    DPI  =   models.CharField(max_length=15)
    nombrecompleto = models.TextField()

    def __str__(self):
        return self.DPI

class Libro(models.Model):

    ISBN    = models.CharField(max_length=15)
    Titulo = models.TextField()
    Autor = models.TextField()
    Editorial = models.TextField()
    Pais = models.TextField()
    year = models.TextField()
    Autores = models.ManyToManyField(Persona, through='Prestamo')

    def __str__(self):
        return self.ISBN

class Prestamo(models.Model):
    prestador = models.ForeignKey(Persona, on_delete=models.CASCADE)
    libroprestado = models.ForeignKey(Libro, on_delete=models.CASCADE)

class PrestaInLine(admin.TabularInline):
    model = Prestamo
    extra = 1

class PersonaAdmin(admin.ModelAdmin):
    inlines = (NotasInLine,)

class LibroAdmin (admin.ModelAdmin):
    inlines = (NotasInLine,)
