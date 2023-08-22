from laboratorio.models import Laboratorio, DirectorGeneral, Producto

#Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.
laboratorio = Laboratorio.objects.all()
print('\n'.join(str(i.nombre) for i in laboratorio))
print('\n'.join(i.nombre for i in laboratorio))


director = DirectorGeneral.objects.all()
print('\n'.join(str(i.nombre) for i in director))

producto = Producto.objects.all()
print('\n'.join(str(i.nombre) for i in producto))


#Obtenga el laboratorio del producto cuyo nombre es 'Producto 1'
query = '''
        SELECT p.id, p.nombre as nombre_producto, l.id, l.nombre as nombre_laboratorio FROM laboratorio_producto p
        INNER JOIN laboratorio_laboratorio l ON p.laboratorio_id = l.id
        WHERE p.nombre = %s;
        '''

consulta = Producto.objects.raw(query, ['Producto 1'])
print('\n'.join(str(i.nombre_laboratorio) for i in consulta))

consulta = Producto.objects.filter(nombre='Producto 1').select_related('laboratorio').values('nombre','laboratorio')
print('\n'.join(str(i.laboratorio) for i in consulta))


consulta = Producto.objects.get(nombre='Producto 1')

producto = Producto.objects.get(nombre='Producto 1')
laboratorio_del_producto = producto.laboratorio
print(f"El laboratorio del Producto 1 es: {laboratorio_del_producto}")
# El laboratorio del Producto 1 es: Laboratorio1


#Ordene todos los productos por nombre, y que muestre los valores de nombre y laboratorio.
consulta = Producto.objects.order_by('nombre').values('nombre','laboratorio')
consulta = Producto.objects.all().order_by('nombre').values('nombre','laboratorio')

#Realice una consulta que imprima por pantalla los laboratorios de todos los productos.
consulta = Producto.objects.all().select_related('laboratorio')
print('\n'.join(str(i.laboratorio) + '-' + (i.nombre) for i in consulta))
print(consulta[0].laboratorio + '-' + consulta[0].nombre)

consulta = Producto.objects.filter(fecha_fabricacion__lte='2023-12-31').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__gte='2023-12-31').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__lt='2023-12-31').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__gt='2023-12-31').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__year__lte='2023').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__year__gte='2023').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__year__lt='2023').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__year__gt='2023').values('nombre', 'p_venta', 'f_fabricacion')
consulta = Producto.objects.filter(fecha_fabricacion__year='2023').values('nombre', 'p_venta', 'f_fabricacion')

consulta = Producto.objects.filter(fecha_fabricacion__gte='2019-01-01', fecha_fabricacion__lte='2021-12-31').values('nombre', 'p_venta', 'f_fabricacion')

consulta = Producto.objects.filter(fecha_fabricacion__year__range=('2019', '2021')).values('nombre', 'p_venta', 'f_fabricacion')