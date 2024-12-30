from django.urls import path
from persona_app.api.views import PersonaAV, PersonaDetalleAV

urlpatterns = [
    path('', PersonaAV.as_view(), name='usuario'),
    path('<int:valor>', PersonaDetalleAV.as_view(), name='detalle'),
]
