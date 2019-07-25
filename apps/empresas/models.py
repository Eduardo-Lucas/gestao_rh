from django.db import models


class Empresa(models.Model):
    """Manutenção do Cadastro de Empresas"""
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    
    def __str__(self):
        return self.nome
