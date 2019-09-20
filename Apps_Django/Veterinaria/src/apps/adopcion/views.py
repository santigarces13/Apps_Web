from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.adopcion.models import Solicitud, Persona

from apps.adopcion.form import SolicitudForm, PersonaForm
from django.core.urlresolvers import reverse_lazy

class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'
    paginate_by = 5

class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')
    @method_decorator(permission_required('adopcion.add_adopcion', reverse_lazy('adopcion:solicitud_listar')))
    def dispatch(self, *args, **kwargs):
        return super(SolicitudCreate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **Kwargs):
        context = super(SolicitudCreate, self).get_context_data(**Kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']= self.second_form_class(self.request.GET)
        return context

    def post(self, request, *arg, **Kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit = False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')
    @method_decorator(permission_required('adopcion.add_adopcion', reverse_lazy('adopcion:solicitud_listar')))
    def dispatch(self, *args, **kwargs):
        return super(SolicitudUpdate, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id = pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2']= self.second_form_class(instance=persona)
        context['id']= pk
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:solicitud_listar')
    @method_decorator(permission_required('adopcion.add_adopcion', reverse_lazy('adopcion:solicitud_listar')))
    def dispatch(self, *args, **kwargs):
        return super(SolicitudUpdate, self).dispatch(*args, **kwargs)
