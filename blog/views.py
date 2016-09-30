from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def listar_articulos(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_articulos.html', {'posts': posts})

def detalle_articulo(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'post': posts})
