from django.shortcuts import render
from .models import Producto

# Create your views here.
def menu(request):
    return render(request, 'menu/menu.html')

def menu(request):
    productos = Producto.objects.all()
    catalogo_productos={'catalogo':productos}
    return render(request, 'menu/menu.html', catalogo_productos)

