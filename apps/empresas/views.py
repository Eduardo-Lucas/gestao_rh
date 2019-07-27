from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from apps.empresas.models import Empresa


class EmpresaCreate(CreateView):
    """Cria uma nova Empresa"""
    model = Empresa
    fields = '__all__'
    
    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok1!')
        
        
class EmpresaEdit(UpdateView):
    """Atualiza uma Empresa existente"""
    model = Empresa
    fields = '__all__'

