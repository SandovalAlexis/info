from django.shortcuts import render

# Create your views here.

def detalles(request):
    context = {}
    return render(request, "blog/detalle.html", context)
