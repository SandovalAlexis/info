from django import db
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    #dni = models.IntegerField(null= None, blank= True)
    
    class Meta:
        db_table = "usuarios"
     
    def __str__(self):
        return self.get_full_name()