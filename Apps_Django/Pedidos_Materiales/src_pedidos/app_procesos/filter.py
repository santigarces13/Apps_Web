#Importaciones necesarias para el archivo.
import django_filters
from app_materiales.models import Articulo

#Clase para filtrar los datos buscados.
class SnippetFilter(django_filters.FilterSet):
    class Meta:
        #Modelo que se va usar para buscar los articulos.
        model = Articulo 
        #Campos que va tener la busqueda.
        fields = {
            'nombre_articulo': ['icontains'],
        }
