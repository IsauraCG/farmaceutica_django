from django.contrib import admin

from .models import Laboratorio, DirectorGeneral, Producto


# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad', 'pais')


class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'especialidad')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'format_date', 'p_costo', 'p_venta')

    def format_date(self, obj):
        return obj.f_fabricacion.strftime('%Y')

    format_date.short_description = 'F FABRICACION'


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
