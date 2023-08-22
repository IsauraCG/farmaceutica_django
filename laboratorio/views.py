# Create your views here.
from django.shortcuts import render

from models import Laboratorio

# Crear controladores-vistas para CRUD
def listar_labs(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listar.html', {'laboratorios': laboratorios})

# Views o controlador para crear laboratorios

# Views o controlador para listar laboratorios

# Views o controlador para editar laboratorios

# Views o controlador para eliminar laboratorios

# Views o controlador para registo de usuarios de la app

# Views o controlador para login de usuarios de la app

# Views o controlador para logout de usuarios de la app

# Views o controlador para index (página principal) sin login
