from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    
    def get_queryset(self):
        """Pega a empresa logada a partir do Usuário logado """
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')

    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')
    
    
class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('hora_extra_list')
    
    form_class = RegistroHoraExtraForm
    
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
