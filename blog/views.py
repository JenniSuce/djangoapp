from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Postear
from django.utils import timezone

def listar_libro(request):
    autor = Postear.objects.all()
    titulo = Postear.objects.all()
    ISBN = Postear.objects.all()
    Portada = Postear.objects.all()
    Editorial = Postear.objects.all()
    pais = Postear.objects.all()
    year= Postear.objects.all()
    return render(request, 'blog/listar_libro.html', {'titulo':titulo})


def post_detail(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def postear_nuevo(request):
    if request.method == "POST":
        formulario = PostearForm(request.POST)
        if formulario.is_valid():
            postear = formulario.save(commit=False)
            postear.autor = request.user
            postear.titulo = request.user
            postear.ISBN = request.user
            postear.Portada = request.user
            postear.Editorial = request.user
            postear.pais = request.user
            postear.years = request.user
            postear.publicacion_date = timezone.now()
            postear.save()
            return redirect('blog.views.post_detail', pk=postear.pk)
    else:
        formulario = PostearForm()
    formulario = PostearForm()
    return render(request, 'blog/editar_libro.html', {'formulario': formulario})
