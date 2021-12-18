from django.shortcuts import render

from django.views.generic.base import TemplateView

from apps.productos.models import Producto
"""
# Inicio basado en funcion 
def inicio(request):
    context = {
        "producto" : Producto.objects.all()
    }
    return render(request, "inicio.html", context)
"""
# Inicio echo en clase que trae heredado la clase templateview, solo le ponemos el nombre que queremos renderizar
class Inicio(TemplateView):
    template_name = "inicio.html"
    
    """"
    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["informacion"] = "Estoy pasando cosas"
        return context
    """