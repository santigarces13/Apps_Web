#Importaciones necesarias para el archivo.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _

#Modelo para crear la tabla Rol_Usuario en la base de datos y generar un modelo para posibles consultas.
class Rol_Usuario(models.Model):
    #Nuevos campos para la tabla.
    codigo_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)
    descripcion_rol = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.nombre_rol)

#Modelo para crear la tabla Area en la base de datos y generar un modelo para posibles consultas.
class Area(models.Model):
    #Nuevos campos para la tabla.
    codigo_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=50)
    descripcion_area = models.CharField(max_length=300)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{}'.format(self.nombre_area)



#Modelo para agregar valores de la tabla user que se usa por defecto en django.
class Usuario(AbstractUser, models.Model):
    #Nuevos campos para la tabla.
    identificacion = models.CharField(max_length=50)
    email = models.EmailField()
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Rol_Usuario).
    roll_r = models.ForeignKey(Rol_Usuario,null=True,blank=False,on_delete=models.CASCADE)
    #Nuevo campo para la tabla(Llave foranea con relación a la tabla Area).
    area_r = models.ForeignKey(Area,null=True,blank=False,on_delete=models.CASCADE)
    #Función que retorna la vizualización de uno varios campos de la tabla.
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)
    class Meta:
        permissions = {
            ('is_instructor', _('Permiso Rol Instructor')),
            ('is_gestor_de_area', _('Permiso Rol Gestor De Area')),
            ('is_cordinador_academico', _('Permiso Rol Cordinador Academico')),
            ('is_coordinador_misional', _('Permiso Rol Coordinador Misional')),
            ('is_subdirector', _('Permiso Rol Subdirector')),
            ('is_almacenista', _('Permiso Rol Almacenista')),
            ('is_administrador', _('Permiso Rol Administrador')),
        }
