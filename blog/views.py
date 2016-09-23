from django.shortcuts import render

# Create your views here.
def listar_articulos(request):
    return render(request, 'blog/listar_articulos.html', {})
