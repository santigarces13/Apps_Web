from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from django.views.generic import View

def listado(request):
    lista = serializers.serialize('json', Mascota.objects.all(), fields=['nombre','sexo'])
    return HttpResponse(lista, content_type='application/json')

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'
    paginate_by = 5

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')
    @method_decorator(permission_required('mascota.add_mascota', reverse_lazy('mascota:mascota_listar')))
    def dispatch(self, *args, **kwargs):
        return super(MascotaCreate, self).dispatch(*args, **kwargs)

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

    @method_decorator(permission_required('mascota.add_mascota', reverse_lazy('mascota:mascota_listar')))
    def dispatch(self, *args, **kwargs):
        return super(MascotaUpdate, self).dispatch(*args, **kwargs)

class MascotaDelete(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')
    @method_decorator(permission_required('mascota.add_mascota', reverse_lazy('mascota:mascota_listar')))
    def dispatch(self, *args, **kwargs):
        return super(MascotaDelete, self).dispatch(*args, **kwargs)

class ReporteMascotPDF(View):
    def cabecera(self, pdf):
        archivo_imagen = settings.STATIC_ROOT+'/img/logoSena.png'
        pdf.drawImage(archivo_imagen, 35, 750, 100, 90, preserveAspectRatio=True)
        pdf.setFont('Helvetica', 16)
        pdf.drawString(230, 790, u"SENA MAS TRABAJO")
        pdf.setFont('Helvetica', 14)
        pdf.drawString(235, 770, u"REPORTE MASCOTAS")


    def tabla(self,pdf,y):
        encabezado = ('Folio', 'Nombre', 'Sexo', 'Fecha rescate')
        detalle = [(mascota.folio, mascota.nombre, mascota.sexo, mascota.fecha_rescate) for mascota in Mascota.objects.all()]
        detalle_orden = Table([encabezado]+ detalle, colWidths = [2* cm, 5 * cm, 5 * cm, 5 * cm])
        detalle_orden.setStyle(TableStyle(
        [
            ('ALING', (0,0), (3,0), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('FONTSIZE', (0,0),(-1,-1),10),
        ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60, y)

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


"""
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')

    else:
        form =MascotaForm()
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('folio')
    contexto = {'mascota': mascota}
    return render(request, 'mascota/mascota_list.html',contexto)

def mascota_edit(request,folio):
    mascota= Mascota.objects.get(folio = folio)
    if request.method == 'GET':
        form= MascotaForm(instance = mascota)
    else:
        form = MascotaForm(request.POST, instance = mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request,folio):
    mascota= Mascota.objects.get(folio = folio)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota_list')
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})
"""
