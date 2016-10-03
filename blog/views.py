from django.shortcuts import render, get_object_or_404
from blog.models import Postear
from django.utils import timezone

# Create your views here.
def listar_articulo(request):
    articulo = Postear.objects.all()
    return render(request, 'blog/listar_articulo.html', {'articulo':articulo})

def post_detail(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
