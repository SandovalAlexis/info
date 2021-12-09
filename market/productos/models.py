from django.db import models

# Create your models here.
#no olvidar lo que entra como parametro 
class prodructo(models.Model): 
    #lo de la igualdad le dice que el model sera tipo caracter con charfiel con un maximo de 250
    nombre = models.CharField(max_length=250),
    
    #le dira al model que es del tipo decimal con nueve digitos y dos decimales
    precio = models.DecimalField(max_digits=9, decimal_places=2) 
    
#luego llevarlo al producto en el settings de market no olvidar!