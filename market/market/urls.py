"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #apartado de auth que nos permite la redireccion de una url a otra
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.inicio, name= "inicio"),
    path('', views.Inicio.as_view(), name= "inicio"),
    
    #Vista de ingreso a login
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name= "login"),
    #Vista de cerrar sesion, Logout
    path('logout/', auth_views.logout_then_login, name= "logout"),
    
    #Include
    path('productos/', include('apps.productos.urls'))
]
