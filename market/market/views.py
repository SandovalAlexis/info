from django.shortcuts import render

from apps.productos.models import Producto

def inicio(request):
    producto = Producto.objects.all()
    
    usuario = {
        "nombre" : "sebastian",
        "apellido" : "sandoval"
    }
    
    context = {
        "usuario" : usuario,
        "producto" : producto
    }
    return render(request, "inicio.html", context)

def login(request):
    return render(request, "login.html")
