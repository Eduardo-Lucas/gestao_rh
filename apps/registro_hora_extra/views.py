from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)

from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    
    def get_queryset(self):
        """Pega a empresa logada a partir do Usuário logado """
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    pass


class HoraExtraDelete(DeleteView):
    pass
    
    
class HoraExtraCreate(CreateView):
    pass
