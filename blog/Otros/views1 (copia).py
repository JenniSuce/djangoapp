#from django.shortcuts import render, get_object_or_404, redirect
#from blog.models import Postear
from django.utils import timezone
#from .forms import PostearForm
# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AlumnosForm
from .models import Cursos, Alumnos, Boleta

def alumno_nuevo(request):
    if request.method == "POST":
        formulario = AlumnosForm(request.POST)
        if formulario.is_valid():
            alumno = Alumnos.objects.create(nombrealumno=formulario.cleaned_data['nombrealumno'], calificaciones = formulario.cleaned_data['calificaciones'])
            for curso_id in request.POST.getlist('curso'):
                boleta = Boleta(curso_id=actor_id, alumno_id = alumno_id)
                boleta.save()
            messages.add_message(request, messages.SUCCESS, 'Alumno Guardado Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'blog/alumno_editar.html', {'formulario': formulario})
#def listar_articulo(request):
#    articulo = Postear.objects.all()
#    return render(request, 'blog/listar_articulo.html', {'articulo':articulo})

def listar_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'blog/lista_alumnos.html', {'nombrepe':pelicula})

def post_detail(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#def postear_nuevo(request):
#    if request.method == "POST":
#        formulario = PostearForm(request.POST)
#        if formulario.is_valid():
#            postear = formulario.save(commit=False)
#            postear.autor = request.user
#            postear.publicacion_date = timezone.now()
#            postear.save()
#            return redirect('blog.views.post_detail', pk=postear.pk)
#    else:
#        formulario = PostearForm()
#    formulario = PostearForm()
#    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})
#def editar_articulo(request, pk):
#    articulo = get_object_or_404(Postear, pk=pk)
#    if request.method == "POST":
#        formulario = PostearForm(request.POST, instance=articulo)
#        if formulario.is_valid():
#            articulo = formulario.save(commit=False)
#            articulo.autor = request.user
#            articulo.save()
#            return redirect('blog.views.post_detail', pk=articulo.pk)
#    else:
#        formulario = PostearForm(instance=articulo)
    #formulario = PostearForm()
#    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})
def alumno_editar(request, pk):
    alumno = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        formulario = PostearForm(request.POST, instance=alumno)
        if formulario.is_valid():
            alumno = formulario.save(commit=False)
            alumno.nombrealumno = request.user
            alumno.save()
            return redirect('blog.views.post_detail', pk=alumno.pk)
    else:
        formulario = PostearForm(instance=pelicula)
    formulario = PostearForm()
    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})


#def pelicula_nueva(request):
#    if request.method == "POST":
#        formulario = PeliculaForm(request.POST)
#        if formulario.is_valid():
#            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
#            for actor_id in request.POST.getlist('actores'):
#               actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
#               actuacion.save()
##       messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
#    else:
#        formulario = PeliculaForm()
#    return render(request, 'blog/editar_pelicula.html', {'formulario': formulario})
