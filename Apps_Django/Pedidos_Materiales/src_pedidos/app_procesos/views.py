#Importaciones necesarias para el archivo.
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_pedido.models import Guia_Pedido, Pedido
from app_usuarios.models import Usuario,Area
from app_materiales.models import Articulo
from app_procesos.forms import PedidoForm,AgregarMaterialForm,ArticuloForm,VerificarExistenciasForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.generic.base import TemplateView
from app_procesos.filter import SnippetFilter


#Importaciones necesarias para reportes PDF.
from django.conf import settings
from django.core import serializers
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from django.views.generic import View



                #####################################
                ###### CASOS PARA PARTICULARES ######
                #####################################
#Clase que determina cual es el primer template que ve un usuario despues del login.
def IndexUsuario(request):
    #Condicional para determinar si es super usuario.
    if request.user.is_superuser:
        #Redireccionamiento para el admin.
        return HttpResponseRedirect('/admin/')
    else:
        #Redireccionamiento para cualquier otro usuario.
        return render(request, 'vistas/inicio.html',{})

#Clase que va listar todos los materiales creados.
class MaterialList(ListView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Articulo
    #El template al cual se va dirigir la clase.
    template_name = 'vistas/listar_materiales.html'
    ##Función la cual va retornar un contexto para el template.
    def get_context_data(self,**kwargs):
        #SQLQuery para hacer la consulta de un pedido en especifico.
        filterr = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        #Los contextos que se le van a enviar al template.
        contexto1 = {'filter':filterr}
        #Retorno de los contextos para que la clase use estos.
        return contexto1

                #####################################
                ##### CASOS PARA GESTOR DE AREA #####
                #####################################

#Clase que crea un articulo.
class ArticuloCreate(CreateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Articulo
    #El template al cual se va dirigir la clase.
    template_name = 'forms/nuevo_articulo_gestor.html'
    #El formulario que va trabajar la clase
    form_class = ArticuloForm
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_materiales')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_gestor_de_area', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(ArticuloCreate, self).dispatch(*args, **kwargs)

#Clase que va a actualizar un articulo.
class ArticuloUpdate(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Articulo
    #El template al cual se va dirigir la clase.
    template_name = 'forms/nuevo_articulo_gestor.html'
    #El formulario que va trabajar la clase
    form_class = ArticuloForm
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_materiales')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_gestor_de_area', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(ArticuloUpdate, self).dispatch(*args, **kwargs)
    #Función la cual va dirigir una vez se complete la accion de la clase.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(ArticuloUpdate, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada
        pk = self.kwargs.get('pk', 0)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context
    #Funcion la cual va a recivir un post del formulario.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        #Variable que almacena el formulario.
        form = self.form_class(request.POST)
        #Validación de formulario.
        if form.is_valid() :
            #Formulario guardado.
            form.save()
            #Retorno de la variable success_url.
            return HttpResponseRedirect(self.get_success_url())
        else:
            #Retorno de la variable success_url.
            return HttpResponseRedirect(self.get_success_url())



                #####################################
                ####### CASOS PARA INSTRUCTOR #######
                #####################################


#Clase que crea el pedido.
class PedidoCreate(CreateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #Nombre del segundo modelo el cual va trabajar la clase.
    second_model = Usuario
    #El template al cual se va dirigir la clase.
    template_name = 'forms/nuevo_pedido.html'
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoCreate, self).dispatch(*args, **kwargs)

#Clase que elimina el pedido.
class PedidoDelete(DeleteView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El template al cual se va dirigir la clase.
    template_name = 'forms/eliminar_pedido.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoDelete, self).dispatch(*args, **kwargs)

#Clase que elimina algun material de algun pedido del instructor.
class MaterialDelete(DeleteView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Pedido
    #El template al cual se va dirigir la clase.
    template_name = 'forms/eliminar_material.html'
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(MaterialDelete, self).dispatch(*args, **kwargs)

    #Función la cual va dirigir una vez se complete la accion de la clase.
    def get_success_url(self):
        #Id de guia_pedido obtenida de la url(<int:pk>).
        idguia=self.kwargs['pk_alt']
        #Retorno del redireccionamiento de url.
        return reverse_lazy('inicio:buscar_pedido', kwargs={'pk': idguia})

    #Función la cual va retornar un contexto para el template.
    def get_context_data(self,**kwargs):
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = Pedido.objects.filter(codigo_pedido=self.kwargs['pk'])
        #SQLQuery para hacer la consulta de una guia de pedido en especifico.
        guia = Guia_Pedido.objects.filter(checkpoint=self.kwargs['pk_alt'])
        #Los contextos que se le van a enviar al template.
        contexto1 = {'pedidos': pedido, 'guias': guia}
        #Retorno de los contextos para que la clase use estos.
        return contexto1

#Clase enviara el pedido del instructor.
class PedidoUpdate(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/enviar_pedido.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoUpdate, self).dispatch(*args, **kwargs)


#Clase que agregara algun material al pedido del instructor.
class AgregarMaterial(CreateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Articulo
    #El template al cual se va dirigir la clase.
    template_name = 'forms/agregar_material.html'
    #El formulario que va trabajar la clase
    form_class = AgregarMaterialForm
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(AgregarMaterial, self).dispatch(*args, **kwargs)
    #Función la cual va dirigir una vez se complete la accion de la clase.
    def get_success_url(self):
        #Id de guia_pedido obtenida de la url(<int:pk>).
        idguia=self.kwargs['pk']
        #Retorno del redireccionamiento de url.
        return reverse_lazy('inicio:agregar_material', kwargs={'pk': idguia})
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self,**kwargs):
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = Guia_Pedido.objects.filter(checkpoint=self.kwargs['pk'])
        #Contexto que va filtrar los datos de materiales.
        filterr = SnippetFilter(self.request.GET, queryset=self.get_queryset())
        #Los contextos que se le van a enviar al template.
        contexto1 = {'pedidos': pedido,'filter':filterr}
        #Retorno de los contextos para que la clase use estos.
        return contexto1

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoList.
@permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index'))
#Función para listar los pedidos.
def PedidoList(request):
    #SQLQuery para hacer la consulta de todos los pedidos que cumplan con los determinados where.
    pedido = Guia_Pedido.objects.filter(responsable_r_id=request.user.id,area_pedido_r=request.user.area_r_id)
    #El contexto que se le va enviar al template.
    contexto1 = {'pedidos': pedido}
    #Retornando un render para visualizar el template listar_pedido.
    return render(request, 'vistas/listar_pedido.html',contexto1)

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoSearch.
@permission_required('app_usuarios.is_instructor', reverse_lazy('inicio:index'))
#Función para buscar un pedido en especifico.
def PedidoSearch(request,pk):
    #SQLQuery para hacer la consulta de un pedido en especifico.
    pedido = Guia_Pedido.objects.filter(checkpoint=pk)
    #SQLQuery para hacer la consulta algun articulo en especifico en el pedido.
    material = Pedido.objects.filter(pedido_guia_r=pk)
    #Los contextos que se le van a enviar al template.
    contexto1 = {'pedidos': pedido, 'materiales':material}
    #Retornando un render para visualizar el template buscar_pedido.
    return render(request, 'vistas/buscar_pedido.html',contexto1)



                    ################################################
                    ####### CASOS PARA COORDINADOR ACADEMICO #######
                    ################################################

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoListAcademico.
@permission_required('app_usuarios.is_cordinador_academico', reverse_lazy('inicio:index'))
#Función para listar los pedidos del coordinador academico.
def PedidoListAcademico(request):
    #SQLQuery para hacer la consulta de todos los pedidos que cumplan con los determinados where.
    pedido = Guia_Pedido.objects.filter(rol_pedido_r=request.user.roll_r_id,area_pedido_r=request.user.area_r_id)
    #El contexto que se le va enviar al template.
    contexto1 = {'pedidos': pedido}
    #Retornando un render para visualizar el template listar_pedido.
    return render(request, 'vistas/pedidos_academico.html',contexto1)

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoSearchAcademico.
@permission_required('app_usuarios.is_cordinador_academico', reverse_lazy('inicio:index'))
#Función para buscar un pedido en especifico del coordinador academico.
def PedidoSearchAcademico(request,pk):
    #SQLQuery para hacer la consulta de un pedido en especifico.
    pedido = Guia_Pedido.objects.filter(checkpoint=pk)
    #SQLQuery para hacer la consulta algun articulo en especifico en el pedido.
    material = Pedido.objects.filter(pedido_guia_r=pk)
    #Los contextos que se le van a enviar al template.
    contexto1 = {'pedidos': pedido, 'materiales':material}
    #Retornando un render para visualizar el template buscar_pedido.
    return render(request, 'vistas/buscar_pedido.html',contexto1)

#Clase para aceptara el pedido(Coordinador academico).
class PedidoUpdateAcademico(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/aceptar_pedido.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_academico')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_cordinador_academico', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoUpdateAcademico, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoUpdateAcademico, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context

#Clase para rechazar el pedido(Coordinador academico).
class PedidoRechazoAcademico(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/rechazar_pedido.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_academico')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_cordinador_academico', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoRechazoAcademico, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoRechazoAcademico, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context


                    ################################################
                    ####### CASOS PARA COORDINADOR MISIONAL ########
                    ################################################

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoListMisional.
@permission_required('app_usuarios.is_coordinador_misional', reverse_lazy('inicio:index'))
#Función para listar los pedidos del coordinador academico.
def PedidoListMisional(request):
    #SQLQuery para hacer la consulta de todos los pedidos que cumplan con los determinados where.
    pedido = Guia_Pedido.objects.filter(rol_pedido_r=request.user.roll_r_id)
    #El contexto que se le va enviar al template.
    contexto1 = {'pedidos': pedido}
    #Retornando un render para visualizar el template listar_pedido.
    return render(request, 'vistas/pedidos_misional.html',contexto1)

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoSearchMisional.
@permission_required('app_usuarios.is_coordinador_misional', reverse_lazy('inicio:index'))
#Función para buscar un pedido en especifico del coordinador misional.
def PedidoSearchMisional(request,pk):
    #SQLQuery para hacer la consulta de un pedido en especifico.
    pedido = Guia_Pedido.objects.filter(checkpoint=pk)
    #SQLQuery para hacer la consulta algun articulo en especifico en el pedido.
    material = Pedido.objects.filter(pedido_guia_r=pk)
    #Variable que se le va asignar todos los valores del pedido.
    precios=0
    #For para sacar todos los valores de los articulos.
    for x in material:
        #SQLQuery para consultar los articulos del pedido.
        articulos = Articulo.objects.filter(codigo_articulo=x.codigo_articulo_r_id)
        #For para sumar todos los valores de los articulos.
        for xx in articulos:
            precios += xx.valor
            #For para sumar las cantidades de los articulos.
            for yy in range(1,x.cantidad_requerida):
                #suma de todos los precios de los productos.
                precios += xx.valor
    #Los contextos que se le van a enviar al template.
    contexto1 = {'pedidos': pedido, 'materiales':material, 'precio':precios}
    #Retornando un render para visualizar el template buscar_pedido.
    return render(request, 'vistas/buscar_pedido.html',contexto1)

#Clase para aceptar el peddido(Coordinador misional).
class PedidoUpdateMisional(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/aceptar_pedido_misional.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_misional')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_coordinador_misional', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoUpdateMisional, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoUpdateMisional, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context

#Clase para rechazar el pedido(Coordinador misional).
class PedidoRechazoMisional(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/rechazar_pedido_misional.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_misional')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_coordinador_misional', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoRechazoMisional, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoRechazoMisional, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context

                    ################################################
                    ########### CASOS PARA SUB DIRECTOR ############
                    ################################################

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoListSubdirector.
@permission_required('app_usuarios.is_subdirector', reverse_lazy('inicio:index'))
#Función para listar los pedidos del coordinador academico.
def PedidoListSubdirector(request):
    #SQLQuery para hacer la consulta de todos los pedidos que cumplan con los determinados where.
    pedido = Guia_Pedido.objects.filter(rol_pedido_r=request.user.roll_r_id)
    #El contexto que se le va enviar al template.
    contexto1 = {'pedidos': pedido}
    #Retornando un render para visualizar el template PedidoListSubdirector.
    return render(request, 'vistas/pedidos_subdirector.html',contexto1)
#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoSearchSubdirector.
@permission_required('app_usuarios.is_subdirector', reverse_lazy('inicio:index'))
#Función para buscar un pedido en especifico del sub director.
def PedidoSearchSubdirector(request,pk):
    #SQLQuery para hacer la consulta de un pedido en especifico.
    pedido = Guia_Pedido.objects.filter(checkpoint=pk)
    #SQLQuery para hacer la consulta algun articulo en especifico en el pedido.
    material = Pedido.objects.filter(pedido_guia_r=pk)
    #Los contextos que se le van a enviar al template.
    contexto1 = {'pedidos': pedido, 'materiales':material}
    #Retornando un render para visualizar el template buscar_pedido.
    return render(request, 'vistas/buscar_pedido.html',contexto1)

#Clase para aceptar el pedido(Subdirector).
class PedidoUpdateSubdirector(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/aceptar_pedido_subdirector.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_subdirector')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_subdirector', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoUpdateSubdirector, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoUpdateSubdirector, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context
#Clase para rechazar el pedido(Subdirector).
class PedidoRechazoSubdirector(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/rechazar_pedido_subdirector.html'
    #La url que se va dirigir una vez que se complete la acción de la clase.
    success_url = reverse_lazy('inicio:listar_pedido_subdirector')
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_subdirector', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(PedidoRechazoSubdirector, self).dispatch(*args, **kwargs)
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(PedidoRechazoSubdirector, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context


                    ################################################
                    ############ CASOS PARA ALMACENISTA ############
                    ################################################

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoListAlmacenista.
@permission_required('app_usuarios.is_almacenista', reverse_lazy('inicio:index'))
#Función para listar los pedidos llegados al almacenista.
def PedidoListAlmacenista(request):
    #SQLQuery para hacer la consulta de todos los pedidos que cumplan con los determinados where.
    pedido = Guia_Pedido.objects.filter(rol_pedido_r=request.user.roll_r_id)
    #El contexto que se le va enviar al template.
    contexto1 = {'pedidos': pedido}
    #Retornando un render para visualizar el template PedidoListSubdirector.
    return render(request, 'vistas/pedidos_almacenista.html',contexto1)

#Función de django donde se verificara si tiene el permiso necesario antes de usar la función PedidoSearchAlmacenista.
@permission_required('app_usuarios.is_almacenista', reverse_lazy('inicio:index'))
#Función para buscar un pedido en especifico del sub director.
def PedidoSearchAlmacenista(request,pk):
    #SQLQuery para hacer la consulta de un pedido en especifico.
    pedido = Guia_Pedido.objects.filter(checkpoint=pk)
    #SQLQuery para hacer la consulta algun articulo en especifico en el pedido.
    material = Pedido.objects.filter(pedido_guia_r=pk)
    #Los contextos que se le van a enviar al template.
    contexto1 = {'pedidos': pedido, 'materiales':material}
    #Retornando un render para visualizar el template buscar_pedido.
    return render(request, 'vistas/buscar_pedido.html',contexto1)

#Clase que verificara existencias de algun pedido.
class VerificarExistencias(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    second_model = Pedido
    #El formulario que va trabajar la clase
    form_class = VerificarExistenciasForm
    #El template al cual se va dirigir la clase.

    template_name = 'forms/verificar_existencias.html'
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_almacenista', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(VerificarExistencias, self).dispatch(*args, **kwargs)
    #Función la cual va dirigir una vez se complete la accion de la clase.
    def get_success_url(self):
        #Id de guia_pedido obtenida de la url(<int:pk>).
        idguia=self.kwargs['pk']
        #Retorno del redireccionamiento de url.
        return reverse_lazy('inicio:verificar_existencias', kwargs={'pk': idguia})

    #Función la cual va retornar un contexto para el template.
    def get_context_data(self,**kwargs):
        #Contexto que se le va enviar al template.
        context = super(VerificarExistencias, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = Guia_Pedido.objects.filter(checkpoint=self.kwargs['pk'])
        #SQLQuery para hacer la consulta de un pedido en especifico.
        material = Pedido.objects.filter(pedido_guia_r_id=self.kwargs['pk'])

        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Contexto para el template.
        context['pedidos']=pedido
        #Contexto para el template.
        context['materiales']=material
        #Retorno de contextos.
        return context

    #Funcion la cual va a recivir un post del formulario.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        #Variable que almacena un valor el cual es codigo_pedido.
        kk = request.POST['codigo_pedido']
        #SQLQuery para hacer la consulta de un pedido en especifico.
        material = Pedido.objects.get(codigo_pedido=kk)
        #Variable que va almacenar el formulario enviado.
        form = self.form_class(request.POST, instance=material)
        #Validación de formulario.
        if form.is_valid():
            #Formulario guardado.
            form.save()
            #Retorno de la variable success_url.
            return HttpResponseRedirect(self.get_success_url())
        else:
            #Retorno de la variable success_url.
            return HttpResponseRedirect(self.get_success_url())


#Clase que modificara el edtado del pedido.
class LlegoPedido(UpdateView):
    #Nombre del modelo el cual va trabajar la clase.
    model = Guia_Pedido
    #El formulario que va trabajar la clase
    form_class = PedidoForm
    #El template al cual se va dirigir la clase.
    template_name = 'forms/llego_pedido.html'
    #Función de django donde se verificara si tiene el permiso necesario para usar esta clase.
    @method_decorator(permission_required('app_usuarios.is_almacenista', reverse_lazy('inicio:index')))
    #Función de django donde es la encargada del punto de entrada para las solicitudes y en última instancia, responsable de devolver la respuesta.
    def dispatch(self, *args, **kwargs):
        return super(LlegoPedido, self).dispatch(*args, **kwargs)
    #Función la cual va dirigir una vez se complete la accion de la clase.
    def get_success_url(self):
        #Id de guia_pedido obtenida de la url(<int:pk>).
        idguia=self.kwargs['pk']
        #Retorno del redireccionamiento de url.
        return reverse_lazy('inicio:buscar_pedido_almacenista', kwargs={'pk': idguia})
    #Función la cual va retornar un contexto para el template.
    def get_context_data(self, **kwargs):
        #Contexto que se le va enviar al template.
        context = super(LlegoPedido, self).get_context_data(**kwargs)
        #Obtención de la llave primaria mandada.
        pk = self.kwargs.get('pk', 0)
        #SQLQuery para hacer la consulta de un pedido en especifico.
        pedido = self.model.objects.get(checkpoint = pk)
        #Validación de formulario.
        if 'form' not in context:
            #Contexto para el template.
            context['form'] = self.form_class()
        #Contexto para el template.
        context['id']= pk
        #Retorno de contextos.
        return context

                    ################################################
                    ################ CASOS PARA PDF ################
                    ################################################


class ReportePedidoPDF(View):
    def cabecera(self, pdf):
        area = Area.objects.filter(codigo_area=self.kwargs['pk_alt'])
        for areas in area:
            nombre_areaa = areas.nombre_area
        print(nombre_areaa)
        archivo_imagen = settings.STATIC_ROOT+'/img/logoSena.jpeg'
        pdf.drawImage(archivo_imagen, 35, 740, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(256, 770, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(230, 750, u"Reporte pedido de "+nombre_areaa+"")


    def tabla(self,pdf,y):
        encabezado = ('Codigo articulo','Nombre articulo', 'Cantidad requerida')

        detalle = [(pedido.codigo_articulo_r.codigo_articulo,pedido.codigo_articulo_r.nombre_articulo, pedido.cantidad_requerida-pedido.existencias) for pedido in Pedido.objects.filter(pedido_guia_r_id=self.kwargs['pk'])if pedido.cantidad_requerida-pedido.existencias>0 ]

        detalle_orden = Table([encabezado]+ detalle, colWidths = [ 2.5 * cm,13.5 * cm, 3 * cm])
        detalle_orden.setStyle(TableStyle(
        [
            ('ALING', (0,0), (2,0), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('FONTSIZE', (0,0),(-1,-1),8),
        ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 30, y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type= 'application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 600
        self.tabla(pdf,y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
