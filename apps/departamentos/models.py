from django.db import models


class Departamento(models.Model):
    """Manutenção do Cadastro de Departamentos"""
    nome = models.CharField(max_length=70, help_text='Nome do departamento')
    
    def __str__(self):
        return self.nome
