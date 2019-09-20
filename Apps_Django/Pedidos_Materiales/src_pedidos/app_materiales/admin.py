#Importaciones necesarias para el archivo.
from django.contrib import admin
from app_materiales.models import Unidad_Metrica,Articulo, Lote,Tipo_Elemento

#Funciones para registrar un modelo para luego poderse visualizar.
admin.site.register(Unidad_Metrica)
admin.site.register(Articulo)
admin.site.register(Lote)
admin.site.register(Tipo_Elemento)