from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Postear
from django.utils import timezone
from .forms import PostearForm

# Create your views here.
def listar_articulo(request):
    articulo = Postear.objects.all()
    return render(request, 'blog/listar_articulo.html', {'articulo':articulo})

def post_detail(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def postear_nuevo(request):
    if request.method == "POST":
        formulario = PostearForm(request.POST)
        if formulario.is_valid():
            postear = formulario.save(commit=False)
            postear.autor = request.user
            postear.publicacion_date = timezone.now()
            postear.save()
            return redirect('blog.views.post_detail', pk=postear.pk)
    else:
        formulario = PostearForm()
    formulario = PostearForm()
    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})

def editar_articulo(request, pk):
    articulo = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        formulario = PostearForm(request.POST, instance=articulo)
        if formulario.is_valid():
            articulo = formulario.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            return redirect('blog.views.post_detail', pk=articulo.pk)
    else:
        formulario = PostearForm(instance=articulo)
    #formulario = PostearForm()
    return render(request, 'blog/editar_articulo.html', {'formulario': formulario})
