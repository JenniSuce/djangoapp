from django.db import models
from django.contrib import admin


class Cursos(models.Model):
    nombrecurso  =   models.CharField(max_length=30)

    def __str__(self):
        return self.nombrecurso

class Alumnos(models.Model):

    nombrealumno    = models.CharField(max_length=60)
    calificaciones = models.TextField()
    Curso = models.ManyToManyField(Cursos, through='Boleta')

    def __str__(self):
        return self.nombrecurso

class Boleta(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)

class NotasInLine(admin.TabularInline):
    model = Boleta
    extra = 1

class CursosAdmin(admin.ModelAdmin):
    inlines = (NotasInLine,)

class AlumnosAdmin (admin.ModelAdmin):
    inlines = (NotasInLine,)
