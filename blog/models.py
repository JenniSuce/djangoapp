from django.db import models
from django.utils import timezone

class Postear(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    ISBN = models.TextField()
    Portada = models.TextField()
    Editorial = models.TextField()
    pais = models.TextField()
    years= models.TextField()
    creacion_date = models.DateTimeField(
                    default=timezone.now)
    publicacion_date = models.DateTimeField(
                        blank=True, null=True)

    def publicar(self):
        self.publicacion_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
