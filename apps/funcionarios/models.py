from django.db import models

from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    """Manutenção do Cadastro de Funcionários"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, models.PROTECT)
    
    def __str__(self):
        return self.nome
