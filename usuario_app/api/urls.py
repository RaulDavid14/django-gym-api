from django.urls import path
from usuario_app.api.views import UsuarioAV, UsuarioDetalleAV

urlpatterns = [
    path('', UsuarioAV.as_view(), name='usuario'),
    path('<int:valor>', UsuarioDetalleAV.as_view(), name='detalle'),
]
