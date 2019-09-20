#Importaciones necesarias para el archivo.
from django.contrib import admin
from app_pedido.models import Estados_Pedido,Guia_Pedido,Pedido

#Funciones para registrar un modelo para luego poderse visualizar.
admin.site.register(Estados_Pedido)
admin.site.register(Guia_Pedido)
admin.site.register(Pedido)
