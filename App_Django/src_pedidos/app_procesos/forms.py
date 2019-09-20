#Importaciones necesarias para el archivo.
from django import forms
from app_pedido.models import Guia_Pedido,Pedido
from app_materiales.models import Articulo

#Clase que va crear un modelo de formulario para crear un pedido.
class PedidoForm(forms.ModelForm):
    class Meta:
        #Modelo para el formulario.
        model = Guia_Pedido
        #Campos que va tener el formulario.
        fields = [
            'fecha_novedad',
            'responsable_r',
            'estado_r',
            'area_pedido_r',
            'rol_pedido_r',
            'nota_pedido',

        ]
        #Etiquetas relacionadas con los campos del formulario.
        labels= {
            'fecha_novedad':'Fecha Creacion de pedido',
            'responsable_r':'Resposable pedido',
            'estado_r' :'Estado de pedido',
            'area_pedido_r' :'Area del pedido',
            'rol_pedido_r' :'Rol del ciclo',
            'nota_pedido': 'Nota del pedido',
        }
        #Tipos de obtención de datos que va tomar los campos necesarios para el formario. 
        widgets = {
            'fecha_novedad': forms.DateInput(),
            'responsable_r': forms.TextInput(),
            'estado_r': forms.TextInput(),
            'area_pedido_r': forms.TextInput(),
            'rol_pedido_r': forms.TextInput(),
            'nota_pedido': forms.Textarea(),
        }
#Clase que va crear un modelo de formulario para agregar un material al pedido.
class AgregarMaterialForm(forms.ModelForm):
    class Meta:
        #Modelo para el formulario.
        model = Pedido
        #Campos que va tener el formulario.
        fields = [
            'fecha_pedido',
            'cantidad_requerida',
            'responsable_r',
            'codigo_articulo_r',
            'pedido_guia_r',

        ]
        #Etiquetas relacionadas con los campos del formulario.
        labels= {
            'fecha_pedido':'Fecha agregado el articulo',
            'cantidad_requerida':'Cantidad',
            'responsable_r' :'Responsable',
            'codigo_articulo_r' :'Articulo',
            'pedido_guia_r' :'Pedido',
        }
        #Tipos de obtención de datos que va tomar los campos necesarios para el formario. 
        widgets = {
            'fecha_pedido': forms.DateInput(),
            'cantidad_requerida': forms.TextInput(),
            'responsable_r': forms.TextInput(),
            'codigo_articulo_r': forms.TextInput(),
            'pedido_guia_r': forms.TextInput(),
        }
#Clase que va crear un modelo de formulario para agregar un articulo al programa.
class ArticuloForm(forms.ModelForm):
    class Meta:
        #Modelo para el formulario.
        model = Articulo
        #Campos que va tener el formulario.
        fields = [
            'codigo_articulo',
            'nombre_articulo',
            'fabricante',
            'ficha_tecnica',
            'valor',
            'unidad_metrica_r',
            'lote_articulo_r',
            'tipo_elemento_r',   
        ]
        #Etiquetas relacionadas con los campos del formulario.
        labels= {
            'codigo_articulo':'Codigo articulo:',
            'nombre_articulo':'Nombre articulo:',
            'fabricante' :'Fabricante:',
            'ficha_tecnica' :'Ficha tecnica:',
            'valor' :'Valor unitario:',
            'unidad_metrica_r':'Unidad metrica:',
            'lote_articulo_r':'Lote articulo:',
            'tipo_elemento_r':'Tipo de elemento:',
        }
        #Tipos de obtención de datos que va tomar los campos necesarios para el formario. 
        widgets = {
            'codigo_articulo': forms.TextInput(),
            'nombre_articulo': forms.TextInput(),
            'fabricante': forms.TextInput(),
            'ficha_tecnica': forms.Textarea(),
            'valor': forms.TextInput(),
            'unidad_metrica_r': forms.Select(),
            'lote_articulo_r': forms.Select(),
            'tipo_elemento_r': forms.Select(),
        }

#Clase que va crear un modelo de formulario para verificar existencias de los productos pedidos.
class VerificarExistenciasForm(forms.ModelForm):
    class Meta:
        #Modelo para el formulario.
        model = Pedido
        #Campos que va tener el formulario.
        fields = [
            'codigo_pedido',
            'fecha_pedido',
            'cantidad_requerida',
            'existencias',
            'responsable_r',
            'codigo_articulo_r',
            'pedido_guia_r',

        ]
        #Etiquetas relacionadas con los campos del formulario.
        labels= {
            'codigo_pedido':'Codigo de pedido',
            'fecha_pedido':'Fecha agregado el articulo',
            'cantidad_requerida':'Cantidad',
            'existencias':'Existencias',
            'responsable_r' :'Responsable',
            'codigo_articulo_r' :'Articulo',
            'pedido_guia_r' :'Pedido',
        }
        #Tipos de obtención de datos que va tomar los campos necesarios para el formario. 
        widgets = {
            'codigo_pedido':forms.TextInput(),
            'fecha_pedido': forms.DateInput(),
            'cantidad_requerida': forms.TextInput(),
            'existencias': forms.TextInput(),
            'responsable_r': forms.TextInput(),
            'codigo_articulo_r': forms.TextInput(),
            'pedido_guia_r': forms.TextInput(),
        }