from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')
    
    def get_absolute_url(self):
        return reverse('funcionario_edit', args=[self.pertence_id])
    
    def __str__(self):
        return self.descricao
