from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('add_empresa', EmpresaCreate.as_view(), name='add_empresa'),
    path('edit_empresa/<int:pk>', EmpresaEdit.as_view(), name='edit_empresa'),
    
]
