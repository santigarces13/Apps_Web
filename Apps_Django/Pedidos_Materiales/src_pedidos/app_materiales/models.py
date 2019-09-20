#Importaciones necesarias para el archivo.
from django.db import models
from app_usuarios.models import Usuario

#Modelo para crear la tabla Unidad_Metrica en la base de datos y generar un modelo para posibles consultas.
class Unidad_Metrica(models.Model):
    #Nuevos campos para la tabla.
    nombre_metrica = models.CharField(max_length=50)
    detalle_metrica = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.nombre_metrica)


#Modelo para crear la tabla Lote en la base de datos y generar un modelo para posibles consultas.
class Lote(models.Model):
    #Nuevos campos para la tabla.
    nombre_lote = models.CharField(primary_key=True,max_length=50)
    detalle_lote = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.nombre_lote)
class Tipo_Elemento(models.Model):
    #Nuevos campos para la tabla.
    nombre_tipo_elemento = models.CharField(primary_key=True,max_length=50)
    detalle_tipo_elemento = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.nombre_tipo_elemento)
#Modelo para crear la tabla Articulo en la base de datos y generar un modelo para posibles consultas.
class Articulo(models.Model):
    #Nuevos campos para la tabla.
    codigo_articulo = models.CharField(primary_key=True,max_length=30)
    nombre_articulo = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=50, null=True,blank=True)
    ficha_tecnica = models.CharField(max_length=500, null=True,blank=True)
    valor = models.IntegerField(null=True,blank=True)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Unidad_Metrica).
    unidad_metrica_r = models.ForeignKey(Unidad_Metrica,null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Lote).
    lote_articulo_r = models.ForeignKey(Lote,null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Tipo_Elemento)
    tipo_elemento_r = models.ForeignKey(Tipo_Elemento,null=True,blank=False,on_delete=models.CASCADE)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{} | {}'.format(self.codigo_articulo ,self.nombre_articulo)
