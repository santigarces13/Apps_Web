#Importaciones necesarias para el archivo.
from django.contrib import admin
from django.urls import path
from app_procesos.views import IndexUsuario, PedidoCreate, PedidoList, PedidoDelete, PedidoSearch, PedidoUpdate,MaterialDelete,MaterialList,AgregarMaterial,PedidoListAcademico,PedidoSearchAcademico,PedidoUpdateAcademico,PedidoRechazoAcademico,PedidoListMisional,PedidoSearchMisional,PedidoUpdateMisional,PedidoRechazoMisional,ArticuloCreate,ArticuloUpdate,PedidoListSubdirector,PedidoSearchSubdirector,PedidoUpdateSubdirector,PedidoRechazoSubdirector,PedidoListAlmacenista,PedidoSearchAlmacenista,VerificarExistencias,LlegoPedido,ReportePedidoPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    ############################# URLS PARTICULARES ##############################
    path('index/', login_required(IndexUsuario), name='index'),
    path('listar_materiales/', login_required(MaterialList.as_view()), name='listar_materiales'),
    ######################### URLS PARA GESTOR DE AREA ###########################
    path('crear_articulo_gestor/', login_required(ArticuloCreate.as_view()), name='crear_articulo_gestor'),
    path('actualizar_articulo_gestor/<str:pk>', login_required(ArticuloUpdate.as_view()), name='actualizar_articulo_gestor'),
    ########################### URLS PARA INSTRUCTOR #############################
    path('crear_pedido/', login_required(PedidoCreate.as_view()), name='crear_pedido'),
    path('buscar_pedido/<int:pk>/', login_required(PedidoSearch), name='buscar_pedido'),
    path('listar_pedido/', login_required(PedidoList), name='listar_pedido'),
    path('eliminar_pedido/<int:pk>/', login_required(PedidoDelete.as_view()), name='eliminar_pedido'),
    path('enviar_pedido/<int:pk>/', login_required(PedidoUpdate.as_view()), name='enviar_pedido'),
    path('eliminar_material/<int:pk>/<int:pk_alt>', login_required(MaterialDelete.as_view()), name='eliminar_material'),
    path('agregar_material/<int:pk>/', login_required(AgregarMaterial.as_view()), name='agregar_material'),
    ####################### URLS PARA COORDINADOR ACADEMICO ######################
    path('listar_pedido_academico/', login_required(PedidoListAcademico), name='listar_pedido_academico'),
    path('buscar_pedido_academico/<int:pk>/', login_required(PedidoSearchAcademico), name='buscar_pedido_academico'),
    path('aceptar_pedido_academico/<int:pk>/', login_required(PedidoUpdateAcademico.as_view()), name='aceptar_pedido_academico'),
    path('rechazar_pedido_academico/<int:pk>/', login_required(PedidoRechazoAcademico.as_view()), name='rechazar_pedido_academico'),
    ####################### URLS PARA COORDINADOR MISIONAL ######################
    path('listar_pedido_misional/', login_required(PedidoListMisional), name='listar_pedido_misional'),
    path('buscar_pedido_misional/<int:pk>/', login_required(PedidoSearchMisional), name='buscar_pedido_misional'),
    path('aceptar_pedido_misional/<int:pk>/', login_required(PedidoUpdateMisional.as_view()), name='aceptar_pedido_misional'),
    path('rechazar_pedido_misional/<int:pk>/', login_required(PedidoRechazoMisional.as_view()), name='rechazar_pedido_misional'),
    ########################## URLS PARA SUB DIRECTOR ##########################
    path('listar_pedido_subdirector/', login_required(PedidoListSubdirector), name='listar_pedido_subdirector'),
    path('buscar_pedido_subdirector/<int:pk>/', login_required(PedidoSearchSubdirector), name='buscar_pedido_subdirector'),
    path('aceptar_pedido_subdirector/<int:pk>/', login_required(PedidoUpdateSubdirector.as_view()), name='aceptar_pedido_subdirector'),
    path('rechazar_pedido_subdirector/<int:pk>/', login_required(PedidoRechazoSubdirector.as_view()), name='rechazar_pedido_subdirector'),
    ########################### URLS PARA ALMACENISTA ##########################
    path('listar_pedido_almacenista/', login_required(PedidoListAlmacenista), name='listar_pedido_almacenista'),
    path('buscar_pedido_almacenista/<int:pk>/', login_required(PedidoSearchAlmacenista), name='buscar_pedido_almacenista'),
    path('verificar_existencias/<int:pk>/', login_required(VerificarExistencias.as_view()), name='verificar_existencias'),
    path('llego_pedido/<int:pk>/', login_required(LlegoPedido.as_view()), name='llego_pedido'),
    ############################### URLS PARA PDF ##############################
    path('reporte_pedido_pdf/<int:pk>/<int:pk_alt>/', login_required(ReportePedidoPDF.as_view()), name = 'reporte_pedido_pdf'),
]
