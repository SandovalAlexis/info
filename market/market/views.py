from django.shortcuts import render

from apps.productos.models import Producto

def inicio(request):
    context = {
        "producto" : Producto.objects.all()
    }
    return render(request, "inicio.html", context)
"""
def login(request):
    
    return render(request, "login.html")
"""