from django.urls import path

from apps.documentos.views import (
    DocumentoCreate,
    DocumentoDelete)

urlpatterns = [
    path('create/<int:funcionario_id>', DocumentoCreate.as_view(), name='documento_create'),
    path('delete/<int:pk>', DocumentoDelete.as_view(), name='documento_delete'),
]
