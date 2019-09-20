#Importaciones necesarias para el archivo.
from django.db import models
from app_usuarios.models import Usuario, Area
from app_materiales.models import Articulo, Lote, Unidad_Metrica
from app_usuarios.models import Rol_Usuario
from datetime import datetime
from django.http import HttpRequest
#Modelo para crear la tabla Estados_Pedido en la base de datos y generar un modelo para posibles consultas.
class Estados_Pedido(models.Model):
    #Nuevos campos para la tabla.
    estado_pedido = models.CharField(primary_key=True,max_length=100)
    descripcion_estado = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.estado_pedido)


#Modelo para crear la tabla Guia_Pedido en la base de datos y generar un modelo para posibles consultas.
class Guia_Pedido(models.Model):
    #Nuevos campos para la tabla.
    checkpoint = models.AutoField(primary_key=True)
    fecha_novedad = models.DateField(default=datetime.now)
    nota_pedido = models.CharField(max_length=500,default="N/A")
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Usuario).
    responsable_r = models.ForeignKey(Usuario, null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Estados_Pedido).
    estado_r = models.ForeignKey(Estados_Pedido, null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Area).
    area_pedido_r = models.ForeignKey(Area,null=True,blank=False,on_delete=models.CASCADE)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    rol_pedido_r = models.ForeignKey(Rol_Usuario,null=True,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return '{}|{}'.format(self.responsable_r,self.estado_r)


#Modelo para crear la tabla Pedido en la base de datos y generar un modelo para posibles consultas.
class Pedido(models.Model):
    #Nuevos campos para la tabla.
    codigo_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField(default=datetime.now)
    cantidad_requerida = models.IntegerField()
    existencias = models.IntegerField(default=0)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Usuario).
    responsable_r = models.ForeignKey(Usuario,null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Articulo).
    codigo_articulo_r  = models.ForeignKey(Articulo,null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Guia_Pedido).
    pedido_guia_r = models.ForeignKey(Guia_Pedido,null=True,blank=False,on_delete=models.CASCADE)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}|{}'.format(self.codigo_articulo_r,self.fecha_pedido)
