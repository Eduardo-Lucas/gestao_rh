from django.urls import path

from apps.\
    registro_hora_extra.\
    views import (HoraExtraList, HoraExtraCreate, HoraExtraEdit, HoraExtraDelete)

urlpatterns = [
    path('list', HoraExtraList.as_view(), name='hora_extra_list'),
    path('create', HoraExtraCreate.as_view(), name='hora_extra_create'),
    path('edit/<int:pk>', HoraExtraEdit.as_view(), name='hora_extra_edit'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='hora_extra_delete'),
]
