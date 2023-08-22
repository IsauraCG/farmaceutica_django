from django.urls import path

from .views import listar_labs

urlpatterns = [
    path('listar_labs/', listar_labs, name='listar_labs'),
]
