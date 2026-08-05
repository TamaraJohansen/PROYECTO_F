from django.shortcuts import render
from .models import Foto

# Create your views here.
def galeria(request):
    return render(request, 'galeria/galeria.html')

def galeria(request):
    fotos = Foto.objects.all()
    catalogo_fotos={'catalogo':fotos}
    return render(request, 'galeria/galeria.html', catalogo_fotos)

