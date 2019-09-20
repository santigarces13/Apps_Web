from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import listado,MascotaList,MascotaCreate, MascotaUpdate, MascotaDelete, ReporteMascotPDF
#from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete
urlpatterns = [
    url(r'^listar', login_required(MascotaList.as_view()), name = 'mascota_listar'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name = 'mascota_crear'),
    url(r'^editar/(?P<pk>[\w]+)$', login_required(MascotaUpdate.as_view()), name = 'mascota_editar'),
    url(r'^eliminar/(?P<pk>[\w]+)$', login_required(MascotaDelete.as_view()), name = 'mascota_eliminar'),
    url(r'^listado', listado, name = 'listado'),
    url(r'^reporte_mascota_pdf', login_required(ReporteMascotPDF.as_view()), name = 'reporte_mascota_pdf'),
]
"""
urlpatterns = [
    url(r'^$', index, name= 'index'),
    url(r'^nuevo$', mascota_view, name = 'mascota_crear'),
    url(r'^listar$', mascota_list, name = 'mascota_listar'),
    url(r'^editar/(?P<folio>[\w]+)$', mascota_edit, name = 'mascota_editar'),
    url(r'^eliminar/(?P<folio>[\w]+)$', mascota_delete, name = 'mascota_eliminar'),
]
"""
