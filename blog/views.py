from django.shortcuts import render
from django.utils import timezone
from .models import Post

def listar_articulos(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_articulos.html', {'posts': posts})
