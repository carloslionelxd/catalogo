from django.shortcuts import render

from productos.models import Producto

def inicio(request):
    template_name = "productos/index.html"
    """
    # query en django para crear registros
    p = Producto.objects.create(
        nombre = "Pantalon",
        precio = 2300,
        descripcion = "Pantalon de Jean Azul"
    )
    """
    # query para ver registros
    productos = Producto.objects.all()

    contexto = {
        'productos': productos}
    return render(request, template_name, contexto)