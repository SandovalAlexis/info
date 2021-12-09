from django.shortcuts import render

def inicio(request):
    producto = [
        {"nombre" : "pantalla", "precio" : 150},
        {"nombre" : "mouse", "precio" : 100}
    ]
    usuario = {
        "nombre" : "sebastian",
        "apellido" : "sandoval"
    }
    
    context = {
        "usuario" : usuario,
        "producto" : producto
    }
    return render(request, "inicio.html", context)