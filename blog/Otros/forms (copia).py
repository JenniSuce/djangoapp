#from django import forms
#from .models import Postear
from django import forms
from .models import Cursos, Alumnos

#class PostearForm(forms.ModelForm):
#    class Meta:
#        model = Postear
#        fields = ('titulo', 'texto',)

class AlumnosForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Alumnos
        fields = ('nombrealumno', 'calificaciones', 'Curso')
#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
    def __init__ (self, *args, **kwargs):
            super(AlumnosForm, self).__init__(*args, **kwargs)
    #En este caso vamos a usar el widget checkbox multiseleccionable.
            self.fields["curso"].widget = forms.widgets.CheckboxSelectMultiple()
    #Podemos usar un texto de ayuda en el widget
            self.fields["curso"].help_text = "Ingrese los Actores que participaron en la película"
    #En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario
            self.fields["curso"].queryset = Cursos.objects.all()
