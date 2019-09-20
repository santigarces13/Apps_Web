from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuarios.form import RegistroForm

class RegistroUsuario(CreateView):
    models = User
    template_name = 'usuarios/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('mascota:mascota_listar')
