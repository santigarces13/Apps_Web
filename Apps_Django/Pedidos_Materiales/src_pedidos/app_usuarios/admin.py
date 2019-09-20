#Importaciones necesarias para el archivo.
from django.contrib import admin
from app_usuarios.models import Rol_Usuario,Area,Usuario
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

#Clase de usuario modificada
class UsuarioAdmin(UserAdmin):
    #El formulario que toma para la creación de usuarios.
    model = Usuario
    #Los campos que se veran al editar el usuario.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('identificacion','email','first_name', 'last_name',)}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
        ('Información de sistema', {'fields': ('roll_r','area_r',)}),)
    #Los campos que se agregaran para la creación de usuarios.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('identificacion','email','first_name', 'last_name', 'username', 'password1', 'password2' ,'roll_r','area_r',),
        }),
    )

#Funciones para registrar un modelo para luego poderse visualizar.
admin.site.register(Rol_Usuario)
admin.site.register(Area)
admin.site.register(Usuario, UsuarioAdmin)
